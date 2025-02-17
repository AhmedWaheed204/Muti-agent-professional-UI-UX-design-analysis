import pytest
from src.models.gemini_model import GeminiModel

def test_gemini_model_initialization():
    model = GeminiModel()
    assert model is not None

def test_gemini_content_generation():
    model = GeminiModel()
    response = model.generate_content("Test prompt")
    assert isinstance(response, str)