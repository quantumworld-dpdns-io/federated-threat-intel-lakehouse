from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter

from src.models.enrichment import EnrichmentCreate, EnrichmentResponse

router = APIRouter()


@router.post("/{ioc_id}", response_model=EnrichmentResponse, status_code=201)
async def enrich_ioc(ioc_id: UUID, payload: EnrichmentCreate):
    enrichment = EnrichmentResponse(**payload.model_dump())
    return enrichment


@router.get("/{ioc_id}")
async def get_enrichments(ioc_id: UUID):
    return {"ioc_id": str(ioc_id), "enrichments": []}
