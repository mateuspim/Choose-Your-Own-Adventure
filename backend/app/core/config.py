from typing import List
from pydantic import BaseSettings
from pydantic import field_validator


class Settings(BaseSettings):
    DATABASE_URL: str

    API_PREFIX: str = "/api"
    DEBUG: bool = True
    ALLOWED_ORIGINS: str = ""

    OPEN_API_KEY: str
    OLLAMA_API_URL: str

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v: str) -> List[str]:
        return [u for u in v.split(",") if u.startswith("http")] if v else []

    class Config:
        env_file: str = ".env"
        env_file_encoding: str = "utf-8"
        case_sensitive: bool = True


settings = Settings()
