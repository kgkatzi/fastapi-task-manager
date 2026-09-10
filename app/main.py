from fastapi import FastAPI

from app.api.tasks import router as tasks_router

app = FastAPI(
    title="Task Manager",
    description=(
        "REST API for task management using FastAPI, PostgreSQL, "
        "SQLAlchemy and Alembic."
    ),
    version="1.0.0",
)

app.include_router(tasks_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}