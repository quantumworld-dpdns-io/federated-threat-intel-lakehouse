from __future__ import annotations

from pydantic import BaseModel, Field

from src.config import settings


class QuantumConfig(BaseModel):
    ibm_token: str = Field(default_factory=lambda: settings.ibm_quantum_token)
    backend: str = Field(default_factory=lambda: settings.ibm_quantum_backend)
    shots: int = 1024
    optimization_level: int = 1
    pqc_enabled: bool = Field(default_factory=lambda: settings.pqc_enabled)
    pqc_algorithm: str = Field(default_factory=lambda: settings.pqc_default_algorithm)
    cudaq_enabled: bool = False
    max_qubits: int = 127
    error_mitigation: bool = True
