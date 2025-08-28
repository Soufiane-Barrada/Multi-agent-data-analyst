"""Configuration settings for the multi-agent data analyst."""

import os
from typing import Optional


class Settings:
    """Application settings and configuration."""
    
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    MODEL_NAME: str = "gpt-4o-mini"
    
    DATA_DIR: str = "data/data"
    
    RESEARCH_AGENT_NAME: str = "researcher"
    ANALYST_AGENT_NAME: str = "analyst"
    
    # Supervisor Configuration
    THREAD_ID: str = "1"
    USER_ID: str = "1"
    
    AVAILABLE_COMPANIES = {
        "AAPL": "Apple",
        "AMZN": "Amazon", 
        "META": "Meta",
        "MSFT": "Microsoft",
        "NFLX": "Netflix",
        "TSLA": "Tesla"
    }


# Global settings instance
settings = Settings() 