FROM python:3.13-slim AS base-uv

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

FROM base-uv AS django

WORKDIR /app

RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

FROM django AS final

COPY ./djangorestframework/pyproject.toml /app/

RUN uv lock && uv sync --frozen --no-dev

COPY ./djangorestframework/ .

CMD ["uv", "run", "uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
