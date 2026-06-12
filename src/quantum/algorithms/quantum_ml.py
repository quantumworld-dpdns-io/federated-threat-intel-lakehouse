from __future__ import annotations

import structlog

logger = structlog.get_logger()


class VariationalQuantumClassifier:
    def __init__(self, num_qubits: int = 4, num_layers: int = 3):
        self._num_qubits = num_qubits
        self._num_layers = num_layers
        self._params: list[float] = []

    def build_circuit(self, features: list[float]) -> dict:
        gates = []
        for _ in range(self._num_layers):
            for i in range(self._num_qubits):
                gates.append({"name": "ry", "qubits": [i], "parameters": [0.0]})
            for i in range(self._num_qubits - 1):
                gates.append({"name": "cx", "qubits": [i, i + 1], "parameters": []})
        return {"name": "vqc", "num_qubits": self._num_qubits, "gates": gates}

    def predict(self, counts: dict[str, int]) -> dict:
        total = sum(counts.values())
        prob_1 = sum(v for k, v in counts.items() if k.endswith("1")) / total
        return {"prediction": 1 if prob_1 > 0.5 else 0, "confidence": abs(prob_1 - 0.5) * 2}


class QuantumKernelEstimation:
    def __init__(self, num_qubits: int = 4):
        self._num_qubits = num_qubits

    def kernel_entry(self, x1: list[float], x2: list[float]) -> float:
        overlap = sum(a * b for a, b in zip(x1[:self._num_qubits], x2[:self._num_qubits]))
        return abs(overlap) ** 2

    def kernel_matrix(self, data: list[list[float]]) -> list[list[float]]:
        n = len(data)
        matrix = [[0.0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = self.kernel_entry(data[i], data[j])
        return matrix
