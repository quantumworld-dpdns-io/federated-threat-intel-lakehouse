from __future__ import annotations

import structlog
from uuid import UUID

from src.config import settings
from src.storage.base import StorageBackend

logger = structlog.get_logger()


class DuckDBStore(StorageBackend):
    def __init__(self):
        self._conn = None
        self._initialized = False

    async def initialize(self) -> None:
        logger.info("Initializing DuckDB store", path=settings.duckdb_path)
        self._initialized = True

    async def create_table(self, name: str, schema: dict) -> None:
        logger.info("Creating DuckDB table", name=name)

    async def insert(self, table: str, records: list[dict]) -> None:
        logger.info("Inserting into DuckDB", table=table, count=len(records))

    async def query(self, sql: str) -> list[dict]:
        logger.debug("Executing DuckDB query", sql=sql[:200])
        return []

    async def get_by_id(self, table: str, record_id: UUID) -> dict | None:
        return None

    async def delete(self, table: str, record_id: UUID) -> bool:
        return True

    async def count(self, table: str) -> int:
        return 0

    async def health_check(self) -> bool:
        return self._initialized
