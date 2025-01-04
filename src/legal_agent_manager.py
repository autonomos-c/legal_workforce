from typing import Dict, Any, List
from enum import Enum
import logging
from datetime import datetime
import sqlite3
import faiss
import numpy as np

class AgentType(Enum):
    DIRECTOR = "director"
    SPECIALIST = "specialist"
    ANALYST = "analyst"
    CASE_MANAGER = "case_manager"
    RISK_ANALYST = "risk_analyst"

class LegalAgentManager:
    def __init__(self):
        self.agents = {}
        self.conversation_context = {}  # Stores ongoing conversation context
        self.memory = {}  # Shared memory between agents
        self.logger = self._setup_logger()
        
        # Initialize embedding model
        from sentence_transformers import SentenceTransformer
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embedding_dim = 384  # Fixed dimension for all-MiniLM-L6-v2
        
        # Initialize FAISS index with correct dimensions
        self.faiss_index = faiss.IndexFlatL2(self.embedding_dim)
        self.logger.info(f"Initialized FAISS index with dimension: {self.embedding_dim}")
        
        # Initialize SQLite database
        self.db_conn = sqlite3.connect('legal_agent_memory.db')
        self._init_db()
        
    def _setup_logger(self):
        logger = logging.getLogger('legal_agent_manager')
        logger.setLevel(logging.DEBUG)  # Changed to DEBUG for more detailed logs
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        return logger

    def register_agent(self, agent_type: AgentType, agent_instance: Any):
        if agent_type in self.agents:
            self.logger.warning(f"Agent {agent_type.value} already registered. Overwriting.")
        self.agents[agent_type] = agent_instance
        self.logger.info(f"Registered agent: {agent_type.value}")

    def handle_request(self, request: Dict) -> Dict:
        self.logger.info(f"Handling request: {request}")
        
        # Update conversation context
        self._update_context(request)
        
        # Determine agent type based on request
        agent_type = self._determine_agent_type(request)
        
        if agent_type not in self.agents:
            return {"error": f"No agent registered for type: {agent_type.value}"}
            
        # Add shared memory and context to request
        request['context_data'] = self.conversation_context
        request['shared_memory'] = self.memory
            
        # Delegate to appropriate agent
        response = self.agents[agent_type].handle(request)
        
        # Update shared memory with agent's response
        self._update_memory(agent_type, response)
        
        return response

    def _update_context(self, request: Dict):
        """Update conversation context with new request data"""
        conversation_id = request.get('conversation_id', 'default')
        if conversation_id not in self.conversation_context:
            self.conversation_context[conversation_id] = {}
            
        # Store last 5 messages per conversation
        if 'messages' not in self.conversation_context[conversation_id]:
            self.conversation_context[conversation_id]['messages'] = []
            
        self.conversation_context[conversation_id]['messages'].append(request)
        if len(self.conversation_context[conversation_id]['messages']) > 5:
            self.conversation_context[conversation_id]['messages'].pop(0)

    def _generate_embedding(self, text: str) -> np.ndarray:
        """Generate embedding from text using Sentence Transformers"""
        embedding = self.embedding_model.encode(text)
        return embedding.reshape(1, -1)  # Asegurar forma 2D

    def _update_memory(self, agent_type: AgentType, response: Dict):
        """Update shared memory with agent's response"""
        memory_key = f"{agent_type.value}_memory"
        if memory_key not in self.memory:
            self.memory[memory_key] = []
            
        # Store last 3 responses per agent type
        self.memory[memory_key].append(response)
        if len(self.memory[memory_key]) > 3:
            self.memory[memory_key].pop(0)
            
        # Generate embedding and store
        response_text = str(response)
        embedding = self._generate_embedding(response_text)
        self.store_embedding(agent_type, embedding, response)

    def _determine_agent_type(self, request: Dict) -> AgentType:
        # Basic routing logic
        if "strategy" in request.get("context", "").lower():
            return AgentType.DIRECTOR
        elif "civil" in request.get("context", "").lower() or "administrative" in request.get("context", "").lower():
            return AgentType.SPECIALIST
        elif "analysis" in request.get("context", "").lower() or "risk" in request.get("context", "").lower():
            return AgentType.ANALYST
        elif "case" in request.get("context", "").lower() or "management" in request.get("context", "").lower():
            return AgentType.CASE_MANAGER
        elif "judicial" in request.get("context", "").lower() or "procedimiento" in request.get("context", "").lower():
            return AgentType.CASE_MANAGER
            
        return AgentType.DIRECTOR  # Default to director

    def _init_db(self):
        """Initialize SQLite database schema"""
        cursor = self.db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory_embeddings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                agent_type TEXT NOT NULL,
                embedding BLOB NOT NULL,
                metadata TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.db_conn.commit()

    def _ensure_2d_shape(self, embedding: np.ndarray) -> np.ndarray:
        """Ensure embedding has correct 2D shape (1, embedding_dim)"""
        if len(embedding.shape) == 1:
            self.logger.debug(f"Reshaping 1D embedding of shape {embedding.shape} to 2D")
            return np.reshape(embedding, (1, self.embedding_dim))
        elif len(embedding.shape) == 2:
            if embedding.shape[0] != 1:
                raise ValueError(f"Primera dimensión debe ser 1, pero es {embedding.shape[0]}")
            if embedding.shape[1] != self.embedding_dim:
                raise ValueError(f"Segunda dimensión debe ser {self.embedding_dim}, pero es {embedding.shape[1]}")
            return embedding
        else:
            raise ValueError(f"Embedding debe ser 1D o 2D, pero tiene forma {embedding.shape}")

    def store_embedding(self, agent_type: AgentType, embedding: np.ndarray, metadata: Dict):
        """Store embedding in FAISS and metadata in SQLite"""
        # Ensure embedding has correct shape and type
        embedding = self._ensure_2d_shape(embedding).astype('float32')
        self.logger.debug(f"Storing embedding with shape {embedding.shape}")
        
        # Add embedding to FAISS index
        self.faiss_index.add(embedding)
        current_index = self.faiss_index.ntotal - 1  # Get the index where it was added
        self.logger.debug(f"FAISS index size after adding: {self.faiss_index.ntotal}")
        
        # Store metadata in SQLite
        cursor = self.db_conn.cursor()
        cursor.execute('''
            INSERT INTO memory_embeddings (agent_type, embedding, metadata)
            VALUES (?, ?, ?)
        ''', (agent_type.value, embedding.tobytes(), str(metadata)))
        self.db_conn.commit()

    def search_similar_embeddings(self, query_embedding: np.ndarray, k: int = 5) -> List[Dict]:
        """Search for similar embeddings using FAISS and retrieve metadata from SQLite"""
        # Ensure query_embedding has correct shape and type
        query_embedding = self._ensure_2d_shape(query_embedding).astype('float32')
        self.logger.debug(f"Searching with query embedding of shape {query_embedding.shape}")
        
        # Search FAISS index
        distances, indices = self.faiss_index.search(query_embedding, k)
        self.logger.debug(f"Search results - distances: {distances}, indices: {indices}")
        
        # Retrieve metadata from SQLite
        cursor = self.db_conn.cursor()
        results = []
        
        # Process each index
        for idx, dist in zip(indices[0], distances[0]):
            if idx == -1:  # Skip invalid results
                continue
                
            # SQLite IDs start at 1, FAISS indices start at 0
            cursor.execute('SELECT * FROM memory_embeddings WHERE rowid = ?', (idx + 1,))
            row = cursor.fetchone()
            if row:
                # Incluir el resultado incluso si la distancia es 0
                results.append({
                    'id': row[0],
                    'agent_type': row[1],
                    'embedding': np.frombuffer(row[2], dtype='float32'),
                    'metadata': eval(row[3]),
                    'timestamp': row[4],
                    'distance': float(dist)  # Add distance for debugging
                })
                self.logger.debug(f"Added result with distance {dist}")
        
        self.logger.debug(f"Found {len(results)} results")
        if results:
            self.logger.debug(f"First result distance: {results[0]['distance']}")
        return results

    def get_status(self) -> Dict:
        return {
            "registered_agents": [agent_type.value for agent_type in self.agents.keys()],
            "active": True,
            "faiss_index_size": self.faiss_index.ntotal,
            "db_records": self.db_conn.execute('SELECT COUNT(*) FROM memory_embeddings').fetchone()[0]
        }
