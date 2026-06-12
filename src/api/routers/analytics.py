from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/iocs-by-type")
async def iocs_by_type():
    return {"data": {}, "message": "IoC distribution by type"}


@router.get("/severity-distribution")
async def severity_distribution():
    return {"data": {}, "message": "Severity distribution"}


@router.get("/top-actors")
async def top_threat_actors():
    return {"data": [], "message": "Top threat actors"}


@router.get("/timeline")
async def threat_timeline():
    return {"data": [], "message": "Threat timeline"}


@router.post("/correlate")
async def correlate_threats(payload: dict):
    return {"data": [], "message": "Correlated threats", "query": payload}
