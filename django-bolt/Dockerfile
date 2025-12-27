# First stage: Install Rust and build wheels
FROM rust:1.83-slim AS builder

# Install Python and build dependencies
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install specific version of maturin that's compatible with Rust 1.83
RUN cargo install maturin --version 0.9.0 --locked

# Final stage with Python
FROM python:3.13-slim

# Copy Rust tools from builder
COPY --from=builder /usr/local/cargo /usr/local/cargo
COPY --from=builder /usr/local/rustup /usr/local/rustup
ENV PATH="/usr/local/cargo/bin:${PATH}"
RUN rustup default stable

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYO3_USE_ABI3_FORWARD_COMPATIBILITY=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    pkg-config \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ./django-bolt/pyproject.toml /app/
RUN uv lock && uv sync --frozen --no-dev

# Copy application code
COPY ./django-bolt/ .

# Run the application
CMD ["uv", "run", "python", "manage.py", "runbolt", "--host", "0.0.0.0", "--port", "8000"]