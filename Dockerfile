# syntax=docker/dockerfile:1
FROM python:3.12-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Poetry installation
RUN pip install poetry

# Copy only requirements to cache dependencies
COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-root --only main

# Copy source
COPY . .

# Entrypoint
ENTRYPOINT ["poetry", "run", "modelica2sysmlv2"]
