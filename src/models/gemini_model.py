import google.generativeai as genai
import os
from dotenv import load_dotenv
from typing import List, Optional

load_dotenv()

class GeminiModel:
    """Wrapper class for Google's Gemini model."""
    
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        """
        Initialize the Gemini model.
        
        Args:
            model_name: Name of the Gemini model to use
        """
        self.api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_content(self, prompt: str, images: Optional[List[str]] = None) -> str:
        """
        Generate content based on text and optional images.
        
        Args:
            prompt: Text prompt for generation
            images: List of image file paths
            
        Returns:
            Generated text content
        """
        try:
            if images:
                image_parts = [self._load_image(img) for img in images]
                response = self.model.generate_content([prompt] + image_parts)
            else:
                response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating content: {str(e)}"

    def _load_image(self, image_path: str) -> genai.types.PartType:
        """Load an image file for Gemini processing."""
        return genai.upload_file(image_path)