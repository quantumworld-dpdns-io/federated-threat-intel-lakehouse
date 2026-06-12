from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class AuditLog(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    actor: str = Field(..., min_length=1)
    action: str = Field(..., min_length=1)
    resource_type: str = Field(..., min_length=1)
    resource_id: UUID
    details: dict = Field(default_factory=dict)
    ip_address: str | None = None

    model_config = {"from_attributes": True}
