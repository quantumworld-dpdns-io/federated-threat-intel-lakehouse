from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter

from src.models.federation import FederatedNodeCreate, FederatedRoundResponse

router = APIRouter()

_nodes: dict[UUID, dict] = {}
_rounds: list[dict] = []


@router.post("/nodes", status_code=201)
async def register_node(payload: FederatedNodeCreate):
    node_id = UUID(bytes=b"\x00" * 16, version=4)
    node = {"id": str(node_id), **payload.model_dump(), "status": "online"}
    _nodes[node_id] = node
    return node


@router.get("/nodes")
async def list_nodes():
    return list(_nodes.values())


@router.get("/rounds")
async def list_rounds():
    return _rounds


@router.post("/rounds", status_code=201)
async def start_round(payload: dict):
    round_data = {
        "round_number": len(_rounds) + 1,
        "status": "in_progress",
        **payload,
    }
    _rounds.append(round_data)
    return round_data


@router.get("/status")
async def federation_status():
    return {
        "total_nodes": len(_nodes),
        "online_nodes": sum(1 for n in _nodes.values() if n.get("status") == "online"),
        "total_rounds": len(_rounds),
        "current_strategy": "fedavg",
    }
