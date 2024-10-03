from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://user:password@localhost:5432/test_project"
    token: str = '7107582390:AAHMeNA5lxuRufPgZUQD5ctzYp4CnvifQv4'

settings = Settings()