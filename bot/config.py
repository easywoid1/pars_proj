import os
from pathlib import Path

from loguru import logger
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("token")

logger_dir = Path(__file__).parent


logger.add(
    f'{os.path.join(logger_dir, "debug.log")}',
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="DEBUG",
)

print(logger_dir)
