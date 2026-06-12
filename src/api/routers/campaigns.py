from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, HTTPException, Query

from src.models.campaign import CampaignCreate, CampaignResponse, CampaignUpdate

router = APIRouter()

_store: dict[UUID, CampaignResponse] = {}


@router.post("", response_model=CampaignResponse, status_code=201)
async def create_campaign(payload: CampaignCreate):
    campaign = CampaignResponse(**payload.model_dump())
    _store[campaign.id] = campaign
    return campaign


@router.get("", response_model=list[CampaignResponse])
async def list_campaigns(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    status: str | None = None,
):
    items = list(_store.values())
    if status:
        items = [c for c in items if c.status.value == status]
    start = (page - 1) * page_size
    return items[start : start + page_size]


@router.get("/{campaign_id}", response_model=CampaignResponse)
async def get_campaign(campaign_id: UUID):
    if campaign_id not in _store:
        raise HTTPException(status_code=404, detail="Campaign not found")
    return _store[campaign_id]


@router.put("/{campaign_id}", response_model=CampaignResponse)
async def update_campaign(campaign_id: UUID, payload: CampaignUpdate):
    if campaign_id not in _store:
        raise HTTPException(status_code=404, detail="Campaign not found")
    existing = _store[campaign_id]
    update_data = payload.model_dump(exclude_unset=True)
    updated = existing.model_copy(update=update_data)
    _store[campaign_id] = updated
    return updated


@router.delete("/{campaign_id}", status_code=204)
async def delete_campaign(campaign_id: UUID):
    if campaign_id not in _store:
        raise HTTPException(status_code=404, detail="Campaign not found")
    del _store[campaign_id]
