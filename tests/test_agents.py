import pytest
from src.models.gemini_model import GeminiModel
from src.agents import VisionAgent, UXAgent, MarketAgent

@pytest.fixture
def mock_model():
    return GeminiModel()

def test_vision_agent_analysis(mock_model):
    agent = VisionAgent(mock_model)
    response = agent.run("Analyze color scheme")
    assert isinstance(response, str)
    assert "color" in response.lower()

def test_ux_agent_analysis(mock_model):
    agent = UXAgent(mock_model)
    response = agent.run("Evaluate navigation flow")
    assert isinstance(response, str)
    assert "navigation" in response.lower()

def test_market_agent_analysis(mock_model):
    agent = MarketAgent(mock_model, tools=[])
    response = agent.run("Analyze competitors")
    assert isinstance(response, str)
    assert "market" in response.lower()