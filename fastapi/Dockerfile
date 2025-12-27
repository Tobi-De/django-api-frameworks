FROM python:3.13-slim AS base-uv

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

FROM base-uv AS fastapi-base

WORKDIR /app

RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

FROM fastapi-base AS final

COPY ./fastapi/pyproject.toml /app/

RUN uv lock && uv sync --frozen --no-dev

COPY ./fastapi/ .

CMD ["uv", "run", "fastapi", "run", "main.py", "--port", "8002"]
