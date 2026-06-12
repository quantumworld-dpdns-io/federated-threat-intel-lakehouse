from __future__ import annotations

import structlog

from src.quantum.config import QuantumConfig

logger = structlog.get_logger()


class QiskitEngine:
    def __init__(self, config: QuantumConfig | None = None):
        self._config = config or QuantumConfig()
        self._backend = None

    async def initialize(self) -> None:
        logger.info(
            "Initializing Qiskit engine",
            backend=self._config.backend,
            shots=self._config.shots,
        )

    async def execute_circuit(self, circuit: dict) -> dict:
        logger.info("Executing quantum circuit", name=circuit.get("name", "unnamed"))
        return {
            "counts": {"0" * circuit.get("num_qubits", 1): self._config.shots},
            "execution_time_ms": 150,
            "backend": self._config.backend,
        }

    async def get_backend_info(self) -> dict:
        return {
            "name": self._config.backend,
            "num_qubits": self._config.max_qubits,
            "status": "available",
        }
