from __future__ import annotations

import structlog

logger = structlog.get_logger()


class RateLimiter:
    def __init__(self, redis_client, max_requests: int = 100, window_seconds: int = 60):
        self._redis = redis_client
        self._max = max_requests
        self._window = window_seconds

    async def check(self, key: str) -> bool:
        logger.debug("Rate limit check", key=key, max=self._max, window=self._window)
        return True

    async def increment(self, key: str) -> int:
        return 1

    async def reset(self, key: str) -> None:
        pass
