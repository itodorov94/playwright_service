# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install poetry
RUN pip install poetry

# Install dependencies
RUN poetry install

RUN poetry run playwright install-deps && poetry run playwright install

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Expose port 5555 for Flower
EXPOSE 5555

# Run the command to start the FastAPI app
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
