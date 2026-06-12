from __future__ import annotations

import structlog

from src.quantum.pqc.liboqs import PQCKeyEncapsulation

logger = structlog.get_logger()


class PQCKeyExchange:
    def __init__(self, algorithm: str = "CRYSTALS-Kyber-768"):
        self._kem = PQCKeyEncapsulation(algorithm)

    def initiate(self) -> dict:
        keypair = self._kem.generate_keypair()
        return {"public_key": keypair["public_key"], "algorithm": self._kem._algorithm}

    def respond(self, peer_public_key: str) -> dict:
        result = self._kem.encapsulate(peer_public_key)
        return {"ciphertext": result["ciphertext"], "shared_secret": result["shared_secret"]}

    def complete(self, ciphertext: str, secret_key: str) -> str:
        return self._kem.decapsulate(ciphertext, secret_key)

    def hybrid_exchange(self, classical_pk: bytes) -> dict:
        pqc = self._kem.generate_keypair()
        return {"classical_pk": classical_pk.hex(), "pqc_pk": pqc["public_key"], "algorithm": "hybrid"}
