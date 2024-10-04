from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres:123@localhost/new_database" #todo сделать норм название с импортами возможно
    token: str = '7107582390:AAHMeNA5lxuRufPgZUQD5ctzYp4CnvifQv4' #todo возможно разнесни на отдельные файлы
    db_echo: bool = True #todo исправить на False


settings = Settings()
