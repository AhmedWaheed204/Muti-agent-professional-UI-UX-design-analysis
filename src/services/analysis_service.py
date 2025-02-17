from typing import List, Dict
from src.agents.agent_factory import AgentFactory

class AnalysisService:
    """Orchestration service for running analyses."""
    
    def __init__(self):
        self.agent_factory = AgentFactory()

    def run_analysis(
        self,
        analysis_types: List[str],
        images: List[str],
        prompt: str,
        context: str
    ) -> Dict[str, str]:
        """
        Run the requested analyses.
        
        Args:
            analysis_types: List of analysis types to perform
            images: List of image paths to analyze
            prompt: User's analysis prompt
            context: Additional context for analysis
            
        Returns:
            Dictionary of analysis results by type
        """
        results = {}
        full_prompt = f"{prompt}\n\nAdditional Context: {context}"

        if "Visual Design" in analysis_types:
            vision_agent = self.agent_factory.create_vision_agent()
            results["visual"] = vision_agent.run(full_prompt, images)

        if "User Experience" in analysis_types:
            ux_agent = self.agent_factory.create_ux_agent()
            results["ux"] = ux_agent.run(full_prompt, images)

        if "Market Analysis" in analysis_types:
            market_agent = self.agent_factory.create_market_agent()
            results["market"] = market_agent.run(full_prompt, images)

        return results