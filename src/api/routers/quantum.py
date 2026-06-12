from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter

from src.models.quantum import QuantumCircuitCreate, QuantumKeyCreate

router = APIRouter()


@router.post("/circuits", status_code=201)
async def create_circuit(payload: QuantumCircuitCreate):
    circuit_id = UUID(bytes=b"\x00" * 16, version=4)
    return {
        "id": str(circuit_id),
        **payload.model_dump(),
        "status": "created",
    }


@router.post("/circuits/{circuit_id}/execute")
async def execute_circuit(circuit_id: UUID):
    return {
        "circuit_id": str(circuit_id),
        "counts": {"0": 512, "1": 512},
        "execution_time_ms": 150,
        "status": "completed",
    }


@router.post("/keys", status_code=201)
async def generate_key(payload: QuantumKeyCreate):
    key_id = UUID(bytes=b"\x00" * 16, version=4)
    return {
        "id": str(key_id),
        **payload.model_dump(),
        "key_material": "base64-encoded-key",
        "status": "generated",
    }


@router.post("/pqc/encrypt")
async def pqc_encrypt(payload: dict):
    return {"ciphertext": "encrypted-data", "algorithm": payload.get("algorithm", "CRYSTALS-Kyber-768")}


@router.post("/pqc/decrypt")
async def pqc_decrypt(payload: dict):
    return {"plaintext": "decrypted-data"}


@router.get("/status")
async def quantum_status():
    return {
        "qiskit_available": True,
        "cudaq_available": False,
        "pqc_enabled": True,
        "default_algorithm": "CRYSTALS-Kyber-768",
    }
