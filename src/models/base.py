from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {"from_attributes": True}


class PaginatedResponse(BaseModel):
    items: list[Any] = Field(default_factory=list)
    total: int = 0
    page: int = 1
    page_size: int = 20
    pages: int = 0


class ErrorResponse(BaseModel):
    detail: str
    error_code: str | None = None
    metadata: dict = Field(default_factory=dict)


class SuccessResponse(BaseModel):
    message: str = "Success"
    data: Any = None
