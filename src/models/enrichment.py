from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from .enums import EnrichmentProvider


class EnrichmentBase(BaseModel):
    ioc_id: UUID
    provider: EnrichmentProvider
    raw_response: dict = Field(default_factory=dict)
    parsed_data: dict = Field(default_factory=dict)


class EnrichmentCreate(EnrichmentBase):
    pass


class EnrichmentResponse(EnrichmentBase):
    id: UUID = Field(default_factory=uuid4)
    fetched_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {"from_attributes": True}


class Enrichment(EnrichmentResponse):
    pass
