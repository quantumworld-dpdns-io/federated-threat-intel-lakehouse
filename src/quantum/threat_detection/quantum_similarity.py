from __future__ import annotations

import structlog

logger = structlog.get_logger()


class QuantumSimilaritySearch:
    def __init__(self, num_qubits: int = 4):
        self._num_qubits = num_qubits

    def ioc_similarity(self, ioc_a: list[float], ioc_b: list[float]) -> float:
        dot = sum(a * b for a, b in zip(ioc_a[:self._num_qubits], ioc_b[:self._num_qubits]))
        norm_a = sum(a**2 for a in ioc_a[:self._num_qubits]) ** 0.5
        norm_b = sum(b**2 for b in ioc_b[:self._num_qubits]) ** 0.5
        return dot / (norm_a * norm_b) if norm_a > 0 and norm_b > 0 else 0.0

    def find_similar(self, target: list[float], candidates: list[list[float]], threshold: float = 0.8) -> list[int]:
        return [i for i, c in enumerate(candidates) if self.ioc_similarity(target, c) > threshold]
