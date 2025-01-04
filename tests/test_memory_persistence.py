import pytest
import numpy as np
from src.legal_agent_manager import LegalAgentManager, AgentType

@pytest.fixture
def manager():
    return LegalAgentManager()

def test_memory_persistence(manager):
    # Test data
    test_response = {"test": "data"}
    
    # Crear embedding con forma correcta (1, 384)
    test_embedding = np.random.rand(384).astype('float32')
    test_embedding = test_embedding.reshape((1, 384))  # Usar reshape con tupla
    
    # Verificar forma antes de store
    assert len(test_embedding.shape) == 2, f"Embedding debe ser 2D, pero tiene forma {test_embedding.shape}"
    assert test_embedding.shape[0] == 1, f"Primera dimensión debe ser 1, pero es {test_embedding.shape[0]}"
    assert test_embedding.shape[1] == 384, f"Segunda dimensión debe ser 384, pero es {test_embedding.shape[1]}"
    
    # Store embedding
    manager.store_embedding(AgentType.DIRECTOR, test_embedding.copy(), test_response)
    
    # Verify storage
    status = manager.get_status()
    assert status['faiss_index_size'] > 0, "FAISS index should not be empty"
    assert status['db_records'] > 0, "SQLite should have records"
    
    # Search similar embeddings usando el mismo embedding
    query_embedding = test_embedding.copy()  # Usar una copia del mismo embedding
    
    # Verificar forma antes de search
    assert len(query_embedding.shape) == 2, f"Embedding debe ser 2D antes de search, pero tiene forma {query_embedding.shape}"
    assert query_embedding.shape[0] == 1, f"Primera dimensión debe ser 1 antes de search, pero es {query_embedding.shape[0]}"
    assert query_embedding.shape[1] == 384, f"Segunda dimensión debe ser 384 antes de search, pero es {query_embedding.shape[1]}"
    
    # Agregar logging para debug
    print(f"\nDEBUG: query_embedding shape: {query_embedding.shape}")
    print(f"DEBUG: query_embedding: {query_embedding}")
    print(f"DEBUG: FAISS index size: {manager.faiss_index.ntotal}")
    
    results = manager.search_similar_embeddings(query_embedding)
    print(f"DEBUG: Found {len(results)} results")
    if len(results) > 0:
        print(f"DEBUG: First result distance: {results[0].get('distance')}")
    
    assert len(results) > 0, "Should find at least one similar embedding"
    assert results[0]['metadata'] == str(test_response), "Metadata should match test response"
