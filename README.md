# Screenshot Service

This project provides a web service for capturing screenshots of web pages and crawling links using FastAPI, Celery, and Playwright. The service allows you to start a crawling process, capture screenshots of the start URL and the first N links, and retrieve the screenshots via a unique task ID.

## Table of Contents

- [Screenshot Service](#screenshot-service)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Directory Structure](#directory-structure)
  - [Usage](#usage)
    - [API Endpoints](#api-endpoints)
      - [Check Service Health](#check-service-health)
      - [Start a Screenshot Task](#start-a-screenshot-task)
      - [Retrieve Screenshots by ID](#retrieve-screenshots-by-id)
      - [Check Task Status](#check-task-status)
    - [Running the service](#running-the-service)

## Features

- Capture screenshots of web pages and their links.
- Asynchronous task processing using Celery.
- API endpoints for starting a screenshot task and retrieving results.

## Architecture

- **FastAPI**: Web framework for the API.
- **Celery**: Distributed task queue for asynchronous processing.
- **Redis**: Message broker for Celery.
- **Playwright**: Browser automation tool for capturing screenshots.

## Setup

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.10 or later.

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/screenshot-service.git
    cd screenshot-service
    ```

2. **Build and run the services using Docker Compose:**

    ```sh
    docker-compose up --build
    ```

3. **Playwright setup:**
    Ensure Playwright installs its required browsers in the Docker container.

### Directory Structure

```sh
screenshot-service/
├── app/
│   ├── __init__.py
│   ├── celery_config.py
│   ├── config.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   ├── tasks.py
|   |── schemas.py
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
├── poetry.lock
└── pyproject.toml
```

## Usage

This section describes how to interact with the service via its API endpoints.

### API Endpoints

#### Check Service Health

- **Endpoint**: `GET /isalive`
- **Description**: Checks if the service is running.
- **Curl Example**:

```bash
  curl http://localhost:8000/isalive
```

#### Start a Screenshot Task

- **Endpoint**: `POST /screenshots`
- **Description**: : Initiates a screenshot capturing task for a given URL and number of links to follow.
- **Request body**:   
```json
  {
  "start_url": "https://example.com",
  "number_of_links": 2
  }
```

- **Curl Example**:
  
```bash
curl -X POST "http://localhost:8000/screenshots" \
-H "Content-Type: application/json" \
-d '{
    "start_url": "https://example.com",
    "number_of_links": 2
}'
```

#### Retrieve Screenshots by ID

- **Endpoint**: `GET /screenshots/{id}`
- **Description**: : Retrieves screenshots associated with a given ID.
- **Curl Example**:
  
```bash
curl http://localhost:8000/screenshots/{id}
```

#### Check Task Status

- **Endpoint**: `/tasks/{task_id}`
- **Description**: : Checks the status of a specific task using the task ID returned by the screenshot endpoint.
- **Curl Example**:
  
```bash
curl http://localhost:8000/tasks/{task_id}
```

### Running the service

Once the application and all its dependencies are running via Docker Compose, you can interact with it through the following exposed services:

- **FastAPI App**: Accessible at http://localhost:8000, where you can make API requests. 