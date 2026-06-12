from __future__ import annotations

import structlog

logger = structlog.get_logger()


class SurfaceCode:
    def __init__(self, distance: int = 3):
        self._distance = distance
        self._num_data_qubits = distance**2
        self._num_syndrome_qubits = (distance - 1)**2

    def encode(self, logical_qubit: int) -> dict:
        return {"logical_qubit": logical_qubit, "physical_qubits": self._num_data_qubits, "distance": self._distance}

    def syndrome_measurement(self) -> dict:
        return {"syndrome_bits": [0] * self._num_syndrome_qubits, "error_detected": False}

    def error_rate(self, physical_error_rate: float) -> float:
        return (physical_error_rate / 0.01) ** ((self._distance + 1) / 2)


class BitFlipCode:
    def encode(self, bit: int) -> list[int]:
        return [bit, bit, bit]

    def decode(self, syndrome: list[int]) -> int:
        return 1 if sum(syndrome) > 1 else 0

    def correct(self, codeword: list[int]) -> list[int]:
        errors = sum(1 for b in codeword if b != codeword[0])
        if errors == 1:
            majority = max(set(codeword), key=codeword.count)
            return [majority] * 3
        return codeword


class PhaseFlipCode:
    def encode(self, bit: int) -> list[str]:
        state = "|+>" if bit == 0 else "|->"
        return [state, state, state]

    def correct(self, states: list[str]) -> str:
        return max(set(states), key=states.count)


class ShorCode:
    def encode(self, bit: int) -> list[list[int]]:
        bf = BitFlipCode()
        return [bf.encode(bit) for _ in range(3)]

    def correct(self, blocks: list[list[int]]) -> int:
        bf = BitFlipCode()
        corrected = [bf.decode(b) for b in blocks]
        return max(set(corrected), key=corrected.count)
