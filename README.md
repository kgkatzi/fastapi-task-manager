# FastAPI Task Manager

A containerized REST API for task management, built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **Alembic**, and **Docker Compose**.

The project demonstrates a clean backend structure with database migrations, request/response validation, dependency injection, CRUD operations, automated tests, and environment-based configuration.

## Tech Stack

* **Python 3.12**
* **FastAPI**
* **Pydantic v2**
* **SQLAlchemy 2.0**
* **PostgreSQL 16**
* **Alembic**
* **Pytest**
* **Docker & Docker Compose**
* **Uvicorn**

## Features

* RESTful CRUD API for task management
* Task creation, retrieval, update, and deletion
* Task completion status and priority levels
* UUID-based task identifiers
* Request and response validation with Pydantic
* Dependency injection for database sessions
* PostgreSQL persistence through SQLAlchemy
* Version-controlled database migrations with Alembic
* Health check endpoint
* Automated API and model tests
* Containerized application and database
* Non-root application user inside the Docker container
* Environment-based application configuration

## Project Structure

```text
fastapi-task-manager/
├── alembic/
│   └── versions/
│       ├── 0001_create_tasks_table.py
│       └── 0002_add_priority_column.py
├── app/
│   ├── api/
│   │   ├── deps.py
│   │   └── tasks.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   ├── schemas/
│   │   └── task.py
│   └── main.py
├── docker/
│   └── entrypoint.sh
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_models.py
│   └── test_tasks.py
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── pytest.ini
└── requirements.txt
```

## API Endpoints

| Method   | Endpoint           | Description    |
| -------- | ------------------ | -------------- |
| `GET`    | `/health`          | Health check   |
| `POST`   | `/tasks`           | Create a task  |
| `GET`    | `/tasks`           | List all tasks |
| `GET`    | `/tasks/{task_id}` | Get a task     |
| `PATCH`  | `/tasks/{task_id}` | Update a task  |
| `DELETE` | `/tasks/{task_id}` | Delete a task  |

### Task Fields

* `id` — UUID
* `title` — required task title
* `description` — optional description
* `completed` — completion status
* `priority` — integer from `0` to `5`
* `created_at` — creation timestamp
* `updated_at` — last update timestamp

## Running with Docker

### 1. Clone the repository

```bash
git clone https://github.com/kgkatzi/fastapi-task-manager.git
cd fastapi-task-manager
```

### 2. Start the application

```bash
docker compose up --build
```

Docker Compose starts:

* PostgreSQL
* FastAPI application
* Alembic database migrations

The application will be available at:

```text
http://localhost:8000
```

Interactive API documentation is available through Swagger UI:

```text
http://localhost:8000/docs
```

## Environment Configuration

For local configuration outside Docker, copy the example environment file:

```bash
cp .env.example .env
```

The `.env` file is intentionally excluded from version control.

## Database Migrations

Alembic manages the database schema.

To apply all migrations:

```bash
alembic upgrade head
```

The project currently contains two migrations:

1. Create the `tasks` table
2. Add the `priority` column

To create a new migration after modifying the SQLAlchemy models:

```bash
alembic revision --autogenerate -m "describe change"
```

Then apply it with:

```bash
alembic upgrade head
```

## Testing

The test suite covers:

* Health endpoint
* Task creation
* Task listing
* Task retrieval
* Missing task handling
* Task updates
* Task deletion
* Request validation
* SQLAlchemy model behavior

Run the tests with:

```bash
pytest
```

The current test suite contains **10 tests**.

## API Example

Create a task:

```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Build a production-style API",
    "priority": 3
  }'
```

Example response:

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "title": "Learn FastAPI",
  "description": "Build a production-style API",
  "priority": 3,
  "completed": false,
  "created_at": "2026-01-01T10:00:00+00:00",
  "updated_at": "2026-01-01T10:00:00+00:00"
}
```

## Architecture

The application follows a simple layered structure:

```text
Client
  │
  ▼
FastAPI Routes
  │
  ▼
Pydantic Schemas
  │
  ▼
SQLAlchemy ORM
  │
  ▼
PostgreSQL
```

Alembic is used separately to manage database schema evolution.

Database sessions are provided to API routes through FastAPI dependency injection, while application configuration is managed with Pydantic Settings.

## Purpose

This project was built to practice backend and software engineering concepts relevant to production-oriented Python applications, including:

* REST API design
* Database modeling
* ORM usage
* Schema validation
* Dependency injection
* Database migrations
* Containerization
* Automated testing
* Application configuration
