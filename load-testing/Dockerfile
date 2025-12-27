FROM python:3.13-slim AS base-uv

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

FROM base-uv AS final

WORKDIR /usr/src/app

COPY ./load-testing/pyproject.toml /usr/src/app/

RUN uv lock && uv sync --frozen --no-dev

COPY ./load-testing/ .

EXPOSE 8089

CMD ["uv", "run", "locust", "--config", "api_response_times.conf"]