FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy dependency files
COPY pyproject.toml ./
RUN uv lock && uv sync --frozen

# Copy application code
COPY . .

# Make wait_for_db.sh executable
RUN chmod +x wait_for_db.sh

# Make port 8009 available to the world outside this container
EXPOSE 8009

# Run the application
CMD ["./wait_for_db.sh", "uv", "run", "python", "manage.py", "runserver", "0.0.0.0:8009"]
