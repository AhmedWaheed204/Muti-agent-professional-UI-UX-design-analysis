import os
import streamlit as st
from dotenv import load_dotenv

class Config:
    """Configuration management class."""
    
    @staticmethod
    def load_environment():
        """Load environment variables from .env file."""
        load_dotenv()

    @staticmethod
    def setup_api_key():
        """Set up API key through Streamlit interface."""
        api_key = st.text_input(
            "Enter Gemini API Key",
            type="password",
            value=os.getenv("GEMINI_API_KEY", "")
        )
        if api_key:
            os.environ["GEMINI_API_KEY"] = api_key

    @staticmethod
    def is_api_configured() -> bool:
        """Check if API key is properly configured."""
        return "GEMINI_API_KEY" in os.environ and os.environ["GEMINI_API_KEY"]