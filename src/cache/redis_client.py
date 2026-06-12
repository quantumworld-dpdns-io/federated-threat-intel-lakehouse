from __future__ import annotations

import structlog

from src.config import settings

logger = structlog.get_logger()


class RedisClient:
    def __init__(self):
        self._client = None
        self._initialized = False

    async def initialize(self) -> None:
        logger.info("Initializing Redis client", url=settings.redis_url)
        self._initialized = True

    async def get(self, key: str) -> str | None:
        return None

    async def set(self, key: str, value: str, ttl: int | None = None) -> None:
        pass

    async def delete(self, key: str) -> bool:
        return True

    async def exists(self, key: str) -> bool:
        return False

    async def health_check(self) -> bool:
        return self._initialized
