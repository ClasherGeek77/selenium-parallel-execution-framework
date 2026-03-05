from enum import Enum
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict

class Environment(str, Enum):
    LOCAL = "local"
    GRID = "grid"
    CLOUD = "cloud"

class BrowserType(str, Enum):
    CHROME = "chrome"
    FIREFOX = "firefox"
    EDGE = "edge"

class Settings(BaseSettings):
    env: Environment = Environment.LOCAL
    browser: BrowserType = BrowserType.CHROME
    headless: bool = True
    
    grid_url: str = "http://localhost:4444/wd/hub"
    
    implicit_wait: int = 10
    page_load_timeout: int = 30
    
    # Model config
    model_config = SettingsConfigDict(
        env_prefix="TEST_",
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
