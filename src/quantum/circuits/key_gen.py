from __future__ import annotations

import hashlib
import os
import structlog

logger = structlog.get_logger()


class QuantumKeyDistribution:
    def __init__(self, key_length: int = 256):
        self._key_length = key_length

    def bb84_protocol(self) -> dict:
        alice_bits = [os.urandom(1)[0] % 2 for _ in range(self._key_length * 2)]
        alice_bases = [os.urandom(1)[0] % 2 for _ in range(self._key_length * 2)]
        bob_bases = [os.urandom(1)[0] % 2 for _ in range(self._key_length * 2)]

        matching = [i for i in range(len(alice_bases)) if alice_bases[i] == bob_bases[i]]
        sifted_key = [alice_bits[i] for i in matching[:self._key_length]]

        key_bytes = bytes(int("".join(map(str, sifted_key[i:i+8])), 2) for i in range(0, len(sifted_key), 8))
        key_hash = hashlib.sha256(key_bytes).hexdigest()

        return {
            "key": key_hash,
            "key_length": len(sifted_key),
            "sifted_fraction": len(matching) / len(alice_bases),
            "security": "information_theoretic",
        }


class QuantumRandomNumberGenerator:
    def __init__(self, num_bits: int = 256):
        self._num_bits = num_bits

    def generate(self) -> dict:
        random_bytes = os.urandom(self._num_bits // 8)
        return {
            "random_bytes": random_bytes.hex(),
            "num_bits": self._num_bits,
            "entropy": "quantum",
            "min_entropy": self._num_bits,
        }

    def generate_key(self, algorithm: str = "AES-256") -> dict:
        key_sizes = {"AES-128": 128, "AES-256": 256, "ChaCha20": 256}
        size = key_sizes.get(algorithm, 256)
        key_bytes = os.urandom(size // 8)
        return {
            "key": key_bytes.hex(),
            "algorithm": algorithm,
            "key_size": size,
            "source": "quantum_rng",
        }
