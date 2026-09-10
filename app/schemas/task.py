import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class TaskBase(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
    )
    priority: int = Field(
        default=0,
        ge=0,
        le=5,
    )


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )
    description: str | None = Field(
        default=None,
        max_length=2000,
    )
    completed: bool | None = None
    priority: int | None = Field(
        default=None,
        ge=0,
        le=5,
    )


class TaskResponse(TaskBase):
    id: uuid.UUID
    completed: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)