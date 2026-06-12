from __future__ import annotations

import structlog

from src.config import settings
from src.storage.base import StorageBackend

logger = structlog.get_logger()


class CacheStore(StorageBackend):
    def __init__(self):
        self._client = None
        self._initialized = False

    async def initialize(self) -> None:
        logger.info("Initializing cache store", url=settings.redis_url)
        self._initialized = True

    async def create_table(self, name: str, schema: dict) -> None:
        pass

    async def insert(self, table: str, records: list[dict]) -> None:
        pass

    async def query(self, sql: str) -> list[dict]:
        return []

    async def get_by_id(self, table: str, record_id: UUID) -> dict | None:
        return None

    async def delete(self, table: str, record_id: UUID) -> bool:
        return True

    async def count(self, table: str) -> int:
        return 0

    async def health_check(self) -> bool:
        return self._initialized

    async def get(self, key: str) -> str | None:
        return None

    async def set(self, key: str, value: str, ttl: int | None = None) -> None:
        pass

    async def delete_key(self, key: str) -> bool:
        return True

    async def exists(self, key: str) -> bool:
        return False
