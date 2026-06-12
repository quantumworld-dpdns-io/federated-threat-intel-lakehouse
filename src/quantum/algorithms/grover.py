from __future__ import annotations

import math
import structlog

logger = structlog.get_logger()


class GroverSearch:
    def __init__(self, num_qubits: int, target_state: str | None = None):
        self._num_qubits = num_qubits
        self._target = target_state or "0" * num_qubits
        self._num_iterations = int(math.pi / 4 * math.sqrt(2**num_qubits))

    def build_oracle(self) -> dict:
        gates = []
        for i in range(self._num_qubits):
            if self._target[i] == "0":
                gates.append({"name": "x", "qubits": [i], "parameters": []})
        if self._num_qubits > 1:
            gates.append({"name": "mcx", "qubits": list(range(self._num_qubits)), "parameters": []})
        for i in range(self._num_qubits):
            if self._target[i] == "0":
                gates.append({"name": "x", "qubits": [i], "parameters": []})
        return {"name": "grover_oracle", "gates": gates}

    def build_diffuser(self) -> dict:
        gates = []
        for i in range(self._num_qubits):
            gates.append({"name": "h", "qubits": [i], "parameters": []})
            gates.append({"name": "x", "qubits": [i], "parameters": []})
        if self._num_qubits > 1:
            gates.append({"name": "mcx", "qubits": list(range(self._num_qubits)), "parameters": []})
        for i in range(self._num_qubits):
            gates.append({"name": "x", "qubits": [i], "parameters": []})
            gates.append({"name": "h", "qubits": [i], "parameters": []})
        return {"name": "grover_diffuser", "gates": gates}

    def search_space_size(self) -> int:
        return 2**self._num_qubits

    def optimal_iterations(self) -> int:
        return self._num_iterations

    def speedup_vs_classical(self) -> float:
        return math.sqrt(2**self._num_qubits)
