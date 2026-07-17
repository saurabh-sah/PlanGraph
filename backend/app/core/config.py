from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class Settings(BaseSettings):
    database_url: PostgresDsn
    graph_context_window: int = 30
    model_config = SettingsConfigDict(
        env_file=BASE_DIR /".env",
        extra="ignore"
    )

settings = Settings()
