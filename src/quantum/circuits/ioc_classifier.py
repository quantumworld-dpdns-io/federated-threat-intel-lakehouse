from __future__ import annotations

import structlog

logger = structlog.get_logger()


class QuantumIoCClassifier:
    def __init__(self, num_qubits: int = 4, num_classes: int = 2):
        self._num_qubits = num_qubits
        self._num_classes = num_classes

    def build_circuit(self, features: list[float]) -> dict:
        gates = []
        for i in range(min(len(features), self._num_qubits)):
            gates.append({"name": "ry", "qubits": [i], "parameters": [features[i]]})
        for i in range(self._num_qubits - 1):
            gates.append({"name": "cx", "qubits": [i, i + 1], "parameters": []})
        return {
            "name": "ioc_classifier",
            "num_qubits": self._num_qubits,
            "depth": len(gates),
            "gates": gates,
            "measurements": [{"qubit": i, "classical_bit": i} for i in range(self._num_qubits)],
        }

    def classify(self, counts: dict[str, int]) -> dict:
        total = sum(counts.values())
        prob_0 = sum(v for k, v in counts.items() if k.count("0") > k.count("1")) / total
        predicted_class = 0 if prob_0 > 0.5 else 1
        confidence = max(prob_0, 1 - prob_0)
        return {"class": predicted_class, "confidence": confidence, "probabilities": {"0": prob_0, "1": 1 - prob_0}}
