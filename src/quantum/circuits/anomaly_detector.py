from __future__ import annotations

import structlog

logger = structlog.get_logger()


class QuantumAnomalyDetector:
    def __init__(self, num_qubits: int = 6):
        self._num_qubits = num_qubits

    def build_encoder(self, features: list[float]) -> dict:
        gates = []
        for i in range(min(len(features), self._num_qubits)):
            gates.append({"name": "ry", "qubits": [i], "parameters": [features[i]]})
        for i in range(self._num_qubits):
            gates.append({"name": "rz", "qubits": [i], "parameters": [features[i] * 0.5]})
        return {"name": "anomaly_encoder", "num_qubits": self._num_qubits, "gates": gates}

    def build_decoder(self) -> dict:
        gates = []
        for i in range(self._num_qubits - 1, 0, -1):
            gates.append({"name": "cx", "qubits": [i - 1, i], "parameters": []})
        for i in range(self._num_qubits):
            gates.append({"name": "ry", "qubits": [i], "parameters": [0.0]})
        return {"name": "anomaly_decoder", "num_qubits": self._num_qubits, "gates": gates}

    def detect(self, reconstruction_fidelity: float, threshold: float = 0.8) -> dict:
        is_anomaly = reconstruction_fidelity < threshold
        return {"is_anomaly": is_anomaly, "fidelity": reconstruction_fidelity, "threshold": threshold}
