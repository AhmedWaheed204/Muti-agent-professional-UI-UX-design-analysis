from src.models.gemini_model import GeminiModel
from .agent import Agent

class UXAgent(Agent):
    """Specialized agent for user experience analysis."""
    
    def __init__(self, model: GeminiModel):
        instructions = [
            "You are a UX analysis expert that:",
            "1. Evaluates user flows and interaction patterns",
            "2. Identifies usability issues and opportunities",
            "3. Suggests UX improvements based on best practices",
            "4. Analyzes accessibility and inclusive design",
            "Focus on user-centric insights and practical improvements"
        ]
        super().__init__(model, instructions, markdown=True)