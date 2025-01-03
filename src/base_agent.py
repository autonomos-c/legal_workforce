from abc import ABC, abstractmethod
from typing import Dict, Any
import logging

class BaseLegalAgent(ABC):
    def __init__(self, agent_type: str):
        self.agent_type = agent_type
        self.logger = self._setup_logger()
        
    def _setup_logger(self):
        logger = logging.getLogger(f'legal_agent_{self.agent_type}')
        logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        return logger

    @abstractmethod
    def handle(self, request: Dict) -> Dict:
        pass

    def validate_request(self, request: Dict) -> bool:
        required_fields = ["context", "question"]
        return all(field in request for field in required_fields)

    def prepare_response(self, content: str, metadata: Dict = None) -> Dict:
        response = {
            "content": content,
            "agent_type": self.agent_type,
            "metadata": metadata or {}
        }
        return response
