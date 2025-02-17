import logging
from typing import Optional

def setup_logger(name: str, log_level: str = "INFO") -> logging.Logger:
    """
    Configure and return a logger instance.
    
    Args:
        name: Logger name
        log_level: Logging level (INFO, DEBUG, etc.)
        
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level.upper())
    return logger

def validate_api_key(api_key: Optional[str]) -> bool:
    """
    Validate the format of a Gemini API key.
    
    Args:
        api_key: API key to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not api_key:
        return False
    return len(api_key) > 30 and api_key.startswith("AI")