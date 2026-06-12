from __future__ import annotations

import structlog

logger = structlog.get_logger()


class QuantumThreatClassifier:
    def __init__(self, num_qubits: int = 8):
        self._num_qubits = num_qubits

    def classify(self, features: list[float]) -> dict:
        score = sum(f**2 for f in features[:self._num_qubits]) / self._num_qubits
        return {
            "threat_level": "high" if score > 0.7 else "medium" if score > 0.4 else "low",
            "confidence": min(score, 1.0),
            "features_used": min(len(features), self._num_qubits),
        }

    def explain(self, features: list[float]) -> dict:
        feature_importance = [(i, f**2) for i, f in enumerate(features[:self._num_qubits])]
        feature_importance.sort(key=lambda x: x[1], reverse=True)
        return {"top_features": feature_importance[:5], "method": "quantum_kernel"}
