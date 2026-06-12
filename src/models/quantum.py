from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class QuantumGate(BaseModel):
    name: str
    qubits: list[int] = Field(..., min_length=1)
    parameters: list[float] = Field(default_factory=list)


class Measurement(BaseModel):
    qubit: int
    classical_bit: int


class QuantumCircuitBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=256)
    num_qubits: int = Field(..., ge=1, le=1024)
    depth: int = Field(..., ge=0)
    gates: list[QuantumGate] = Field(default_factory=list)
    measurements: list[Measurement] = Field(default_factory=list)
    backend: str = "statevector_simulator"
    shots: int = Field(1024, ge=1, le=100000)


class QuantumCircuitCreate(QuantumCircuitBase):
    pass


class QuantumCircuitResponse(QuantumCircuitBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {"from_attributes": True}


class QuantumCircuit(QuantumCircuitResponse):
    pass


class QuantumResultResponse(BaseModel):
    circuit_id: UUID
    counts: dict[str, int] = Field(default_factory=dict)
    metadata: dict = Field(default_factory=dict)
    execution_time_ms: int = 0

    model_config = {"from_attributes": True}


class QuantumResult(QuantumResultResponse):
    pass


class QuantumKeyBase(BaseModel):
    algorithm: str = "CRYSTALS-Kyber-768"
    key_size: int = Field(256, ge=128, le=4096)


class QuantumKeyCreate(QuantumKeyBase):
    pass


class QuantumKeyResponse(QuantumKeyBase):
    id: UUID = Field(default_factory=uuid4)
    key_material: bytes = b""
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: datetime | None = None

    model_config = {"from_attributes": True}


class QuantumKey(QuantumKeyResponse):
    pass
