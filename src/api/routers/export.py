from __future__ import annotations

from fastapi import APIRouter, Query
from fastapi.responses import Response

router = APIRouter()


@router.get("/stix")
async def export_stix():
    bundle = {
        "type": "bundle",
        "id": "bundle--export",
        "spec_version": "2.1",
        "objects": [],
    }
    return bundle


@router.get("/csv")
async def export_csv():
    content = "ioc_type,value,severity,confidence,tlp,source\n"
    return Response(content=content, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=iocs.csv"})


@router.get("/parquet")
async def export_parquet():
    return Response(content=b"", media_type="application/octet-stream")
