from src.models.gemini_model import GeminiModel
from .agent import Agent

class MarketAgent(Agent):
    """Specialized agent for market research analysis."""
    
    def __init__(self, model: GeminiModel, tools: list = None):
        instructions = [
            "You are a market research expert that:",
            "1. Identifies market trends and competitor patterns",
            "2. Analyzes similar products and features",
            "3. Suggests market positioning and opportunities",
            "4. Provides industry-specific insights",
            "Focus on actionable market intelligence"
        ]
        super().__init__(model, instructions, tools=tools, markdown=True)