import sys
from pathlib import Path
import logging

# Agregar directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

from src.legal_agent_manager import LegalAgentManager, AgentType
from src.director_agent import DirectorAgent
from src.specialist_agent import SpecialistAgent
from src.analyst_agent import AnalystAgent

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    
    # Create manager instance
    manager = LegalAgentManager()
    
    # Register agents
    director = DirectorAgent()
    specialist = SpecialistAgent()
    analyst = AnalystAgent()
    manager.register_agent(AgentType.DIRECTOR, director)
    manager.register_agent(AgentType.SPECIALIST, specialist)
    manager.register_agent(AgentType.ANALYST, analyst)
    
    # Test requests
    test_requests = [
        {
            "context": "Estrategia de cumplimiento normativo",
            "question": "¿Cómo asegurar que un modelo de IA cumple con las normativas chilenas?"
        },
        {
            "context": "Derecho civil chileno",
            "question": "¿Cómo redactar un recurso administrativo para un caso de derecho de familia?"
        },
        {
            "context": "Análisis de riesgos legales",
            "question": "¿Cuáles son los principales riesgos legales al implementar un sistema de IA en el sector financiero?"
        }
    ]
    
    for test_request in test_requests:
    
        response = manager.handle_request(test_request)
        print("\nResponse from manager:")
        print(response)

if __name__ == "__main__":
    main()
