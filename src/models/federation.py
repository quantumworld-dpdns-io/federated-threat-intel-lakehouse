from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from .enums import NodeStatus, RoundStatus


class FederatedNodeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=256)
    organization: str = Field(..., min_length=1, max_length=256)
    endpoint: str = Field(..., min_length=1)


class FederatedNodeCreate(FederatedNodeBase):
    pass


class FederatedNodeResponse(FederatedNodeBase):
    id: UUID = Field(default_factory=uuid4)
    status: NodeStatus = NodeStatus.OFFLINE
    last_heartbeat: datetime = Field(default_factory=datetime.utcnow)
    data_samples: int = 0
    model_version: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {"from_attributes": True}


class FederatedNode(FederatedNodeResponse):
    pass


class FederatedRoundBase(BaseModel):
    round_number: int
    strategy: str = "fedavg"
    participants: list[UUID] = Field(default_factory=list)


class FederatedRoundResponse(FederatedRoundBase):
    started_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: datetime | None = None
    loss: float | None = None
    accuracy: float | None = None
    privacy_epsilon: float | None = None
    status: RoundStatus = RoundStatus.PENDING

    model_config = {"from_attributes": True}


class FederatedRound(FederatedRoundResponse):
    pass


class ModelUpdateBase(BaseModel):
    node_id: UUID
    round_number: int
    num_samples: int
    loss: float
    accuracy: float | None = None


class ModelUpdateResponse(ModelUpdateBase):
    id: UUID = Field(default_factory=uuid4)
    parameters: bytes = b""
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {"from_attributes": True}


class ModelUpdate(ModelUpdateResponse):
    pass
