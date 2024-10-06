FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-dev

COPY ../main.py .

CMD ["poetry", "run", "python", "bot.py"]
