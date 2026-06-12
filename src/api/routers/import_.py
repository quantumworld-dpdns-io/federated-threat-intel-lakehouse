from __future__ import annotations

from fastapi import APIRouter, UploadFile

router = APIRouter()


@router.post("/stix")
async def import_stix(payload: dict):
    return {"imported": 0, "message": "STIX import endpoint"}


@router.post("/csv")
async def import_csv(file: UploadFile):
    return {"imported": 0, "message": "CSV import endpoint"}
