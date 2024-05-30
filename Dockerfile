# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install poetry
# Install system dependencies for playwright separately to avoid reinstalling every time dependencies change
RUN pip install poetry && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        libglib2.0-0 libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 libcups2 libdbus-1-3 \
        libxkbcommon0 libxdamage1 libxcomposite1 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 \
        libasound2 libxshmfence1 && \
    rm -rf /var/lib/apt/lists/*

# Copy only poetry.lock and pyproject.toml to install dependencies
COPY pyproject.toml poetry.lock ./

# Install Python dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Install playwright specific dependencies
RUN poetry run playwright install-deps && \
    poetry run playwright install

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000 for the FastAPI app
EXPOSE 8000
