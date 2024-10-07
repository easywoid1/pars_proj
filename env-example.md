# .env.example

# Токен вашего бота Telegram
token=Токен вашего бота

# URL вашего бота в Telegram (не используется в настоящий момент)
name=

# URL для подключения к базе данных PostgreSQL
# Пример использования при запуске в контейнере Docker

# db_url="postgresql+asyncpg://postgres:123@db/new_database"

# Пароль для базы данных PostgreSQL
POSTGRES_PASSWORD=123

# URL для подключения к базе данных при локальном запуске
db_url="postgresql+asyncpg://postgres:123@localhost/new_database"
