import os
from dataclasses import dataclass
from typing import List

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    app_host: str = os.getenv("APP_HOST", "0.0.0.0")
    app_port: int = int(os.getenv("APP_PORT", "8000"))
    model_name: str = os.getenv("MODEL_NAME", "gpt-4o-mini")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    allowed_origins: List[str] = (os.getenv("ALLOWED_ORIGINS", "http://localhost:3000,http://localhost:8000").split(","))


settings = Settings()
