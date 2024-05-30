# Screenshot Service

This project provides a web service for capturing screenshots of web pages and crawling links using FastAPI, Celery, and Playwright. The service allows you to start a crawling process, capture screenshots of the start URL and the first N links, and retrieve the screenshots via a unique task ID.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
  - [Running the Services](#running-the-services)
- [Monitoring](#monitoring)
- [Contributing](#contributing)
- [License](#license)

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