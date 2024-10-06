import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
import os

from loguru import logger
from dotenv import load_dotenv

load_dotenv()
logger_dir = Path(__file__).parent
logger.add(
    f'{os.path.join(logger_dir, "debug.log")}',
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra='allow'
    )
    db_url: str
    token: str
    db_echo: bool = True  # todo исправить на False


settings = Settings()