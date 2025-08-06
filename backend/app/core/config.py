# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    # Database config
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    # OpenAI config
    OPENAI_API_KEY: str
    OPENAI_MODEL: str
    OPENAI_API_BASE: str

    # App config
    API_HOST: str
    API_PORT: int
    ENVIRONMENT: str
    APP_NAME: str
    LOG_LEVEL: str

    # Vector DB
    VECTOR_DB_TYPE: str
    VECTOR_STORE_PATH: str

    # Upload
    UPLOAD_DIR: str

    # Memory
    MEMORY_WINDOW_SIZE: int

    # Construct DATABASE_URL from parts (do NOT put in .env)
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(
        env_file=".env",   # Load environment variables from this file
        extra="ignore"     # Ignore unneeded variables in the .env file
    )

@lru_cache()
def get_settings() -> Settings:
    return Settings()  

settings = get_settings()# Automatically loads from .env
