from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ThreatActorBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=256)
    aliases: list[str] = Field(default_factory=list)
    description: str = Field(..., min_length=1)
    motivation: str | None = None
    sophistication: str | None = None
    resource_level: str | None = None
    country: str | None = None
    tags: list[str] = Field(default_factory=list)


class ThreatActorCreate(ThreatActorBase):
    pass


class ThreatActorUpdate(BaseModel):
    name: str | None = None
    aliases: list[str] | None = None
    description: str | None = None
    motivation: str | None = None
    sophistication: str | None = None
    resource_level: str | None = None
    country: str | None = None
    tags: list[str] | None = None


class ThreatActorResponse(ThreatActorBase):
    id: UUID = Field(default_factory=uuid4)
    first_seen: datetime = Field(default_factory=datetime.utcnow)
    last_seen: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {"from_attributes": True}


class ThreatActor(ThreatActorResponse):
    pass
