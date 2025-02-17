from src.models.gemini_model import GeminiModel
from .vision_agent import VisionAgent
from .ux_agent import UXAgent
from .market_agent import MarketAgent
from src.tools.duckduckgo_tools import DuckDuckGoTools

class AgentFactory:
    """Factory class for creating analysis agents."""
    
    def __init__(self):
        self.model = GeminiModel()
        self.search_tool = DuckDuckGoTools()

    def create_vision_agent(self) -> VisionAgent:
        """Create a Vision Analysis agent."""
        return VisionAgent(model=self.model)

    def create_ux_agent(self) -> UXAgent:
        """Create a UX Analysis agent."""
        return UXAgent(model=self.model)

    def create_market_agent(self) -> MarketAgent:
        """Create a Market Research agent with search capabilities."""
        return MarketAgent(model=self.model, tools=[self.search_tool])