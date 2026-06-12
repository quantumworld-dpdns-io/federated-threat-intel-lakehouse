from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, HTTPException, Query

from src.models.vulnerability import (
    VulnerabilityCreate,
    VulnerabilityResponse,
    VulnerabilityUpdate,
)

router = APIRouter()

_store: dict[UUID, VulnerabilityResponse] = {}


@router.post("", response_model=VulnerabilityResponse, status_code=201)
async def create_vulnerability(payload: VulnerabilityCreate):
    vuln = VulnerabilityResponse(**payload.model_dump())
    _store[vuln.id] = vuln
    return vuln


@router.get("", response_model=list[VulnerabilityResponse])
async def list_vulnerabilities(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    severity: str | None = None,
):
    items = list(_store.values())
    if severity:
        items = [v for v in items if v.severity.value == severity]
    start = (page - 1) * page_size
    return items[start : start + page_size]


@router.get("/{vuln_id}", response_model=VulnerabilityResponse)
async def get_vulnerability(vuln_id: UUID):
    if vuln_id not in _store:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    return _store[vuln_id]


@router.put("/{vuln_id}", response_model=VulnerabilityResponse)
async def update_vulnerability(vuln_id: UUID, payload: VulnerabilityUpdate):
    if vuln_id not in _store:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    existing = _store[vuln_id]
    update_data = payload.model_dump(exclude_unset=True)
    updated = existing.model_copy(update=update_data)
    _store[vuln_id] = updated
    return updated


@router.delete("/{vuln_id}", status_code=204)
async def delete_vulnerability(vuln_id: UUID):
    if vuln_id not in _store:
        raise HTTPException(status_code=404, detail="Vulnerability not found")
    del _store[vuln_id]
