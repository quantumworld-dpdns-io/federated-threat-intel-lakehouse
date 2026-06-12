from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from .enums import CampaignStatus, Severity


class CampaignBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=256)
    description: str = Field(..., min_length=1)
    severity: Severity = Severity.MEDIUM
    status: CampaignStatus = CampaignStatus.ACTIVE
    threat_actor_id: UUID | None = None
    tags: list[str] = Field(default_factory=list)
    mitre_tactics: list[str] = Field(default_factory=list)


class CampaignCreate(CampaignBase):
    pass


class CampaignUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    severity: Severity | None = None
    status: CampaignStatus | None = None
    threat_actor_id: UUID | None = None
    tags: list[str] | None = None
    mitre_tactics: list[str] | None = None


class CampaignResponse(CampaignBase):
    id: UUID = Field(default_factory=uuid4)
    first_seen: datetime = Field(default_factory=datetime.utcnow)
    last_seen: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {"from_attributes": True}


class Campaign(CampaignResponse):
    pass
