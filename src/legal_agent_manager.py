from typing import Dict, Any
from enum import Enum
import logging

class AgentType(Enum):
    DIRECTOR = "director"
    SPECIALIST = "specialist"
    ANALYST = "analyst"
    CASE_MANAGER = "case_manager"
    RISK_ANALYST = "risk_analyst"

class LegalAgentManager:
    def __init__(self):
        self.agents = {}
        self.logger = self._setup_logger()
        
    def _setup_logger(self):
        logger = logging.getLogger('legal_agent_manager')
        logger.setLevel(logging.INFO)
        
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
        
        # Determine agent type based on request
        agent_type = self._determine_agent_type(request)
        
        if agent_type not in self.agents:
            return {"error": f"No agent registered for type: {agent_type.value}"}
            
        # Delegate to appropriate agent
        response = self.agents[agent_type].handle(request)
        return response

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

    def get_status(self) -> Dict:
        return {
            "registered_agents": [agent_type.value for agent_type in self.agents.keys()],
            "active": True
        }
