from src.models.gemini_model import GeminiModel
from .agent import Agent

class VisionAgent(Agent):
    """Specialized agent for visual design analysis."""
    
    def __init__(self, model: GeminiModel):
        instructions = [
            "You are a visual analysis expert that:",
            "1. Identifies design elements, patterns, and visual hierarchy",
            "2. Analyzes color schemes, typography, and layouts",
            "3. Detects UI components and their relationships",
            "4. Evaluates visual consistency and branding",
            "Be specific and technical in your analysis"
        ]
        super().__init__(model, instructions, markdown=True)