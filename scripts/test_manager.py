# Deshabilitar logging completamente antes de cualquier import
import logging
logging.disable(logging.CRITICAL)

# Deshabilitar todos los loggers existentes
for logger_name in logging.root.manager.loggerDict:
    logging.getLogger(logger_name).disabled = True
    logging.getLogger(logger_name).propagate = False

import sys
from pathlib import Path

# Agregar directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

from src.legal_agent_manager import LegalAgentManager, AgentType
from src.director_agent import DirectorAgent
from src.specialist_agent import SpecialistAgent
from src.analyst_agent import AnalystAgent
from src.case_manager_agent import CaseManagerAgent

def main():
    
    # Create manager instance
    manager = LegalAgentManager()
    print("\n=== Sistema de Agentes Legales AI ===")
    
    # Register agents
    director = DirectorAgent()
    specialist = SpecialistAgent()
    analyst = AnalystAgent()
    case_manager = CaseManagerAgent()
    manager.register_agent(AgentType.DIRECTOR, director)
    manager.register_agent(AgentType.SPECIALIST, specialist)
    manager.register_agent(AgentType.ANALYST, analyst)
    manager.register_agent(AgentType.CASE_MANAGER, case_manager)
    
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
        },
        {
            "context": "Procedimiento judicial",
            "question": "¿Cómo gestionar un caso de demanda por incumplimiento de contrato?"
        }
    ]
    
    for test_request in test_requests:
    
        response = manager.handle_request(test_request)
        print(f"\n=== Respuesta del Agente {response['agent_type'].upper()} ===")
        print(response['content'])
        print("\n" + "="*50)

if __name__ == "__main__":
    main()
