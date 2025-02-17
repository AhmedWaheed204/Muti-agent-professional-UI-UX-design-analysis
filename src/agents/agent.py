from typing import List, Optional
from src.models.gemini_model import GeminiModel

class Agent:
    """Base class for all analysis agents."""
    
    def __init__(
        self,
        model: GeminiModel,
        instructions: List[str],
        tools: Optional[List] = None,
        markdown: bool = True
    ):
        """
        Initialize an Agent instance.
        
        Args:
            model: Gemini model instance
            instructions: List of expert instructions
            tools: List of available tools
            markdown: Whether to format output as markdown
        """
        self.model = model
        self.instructions = instructions
        self.tools = tools if tools else []
        self.markdown = markdown

    def run(self, message: str, images: Optional[List[str]] = None) -> str:
        """
        Execute the agent's analysis workflow.
        
        Args:
            message: User's analysis request
            images: List of image paths to analyze
            
        Returns:
            Analysis results as formatted string
        """
        full_prompt = self._build_prompt(message)
        response = self.model.generate_content(full_prompt, images)
        return self._format_response(response)

    def _build_prompt(self, message: str) -> str:
        """Construct the full analysis prompt."""
        prompt = "\n".join(self.instructions)
        prompt += f"\n\nUser Request: {message}"
        
        if self.tools:
            prompt += "\n\nAdditional Context:"
            for tool in self.tools:
                if hasattr(tool, "search"):
                    results = tool.search(message)
                    prompt += f"\nSearch Results:\n{results}"
        return prompt

    def _format_response(self, response: str) -> str:
        """Format the final response."""
        return f"```markdown\n{response}\n```" if self.markdown else response