from __future__ import annotations

import structlog

logger = structlog.get_logger()


class IoCCache:
    def __init__(self, redis_client):
        self._redis = redis_client
        self._prefix = "ioc"

    async def get_ioc(self, ioc_type: str, value: str) -> dict | None:
        key = f"{self._prefix}:{ioc_type}:{value}"
        return await self._redis.get(key)

    async def set_ioc(self, ioc_type: str, value: str, data: dict, ttl: int = 3600) -> None:
        key = f"{self._prefix}:{ioc_type}:{value}"
        await self._redis.set(key, str(data), ttl=ttl)

    async def invalidate(self, ioc_type: str, value: str) -> None:
        key = f"{self._prefix}:{ioc_type}:{value}"
        await self._redis.delete(key)

    async def warm_from_source(self, iocs: list[dict]) -> int:
        count = 0
        for ioc in iocs:
            await self.set_ioc(ioc["ioc_type"], ioc["value"], ioc)
            count += 1
        return count
