from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/iocs")
async def stream_iocs():
    return {"message": "IoC stream endpoint - use WebSocket for real-time"}


@router.get("/alerts")
async def stream_alerts():
    return {"message": "Alert stream endpoint - use WebSocket for real-time"}
