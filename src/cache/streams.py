from __future__ import annotations

import structlog

logger = structlog.get_logger()


class StreamManager:
    def __init__(self, redis_client):
        self._redis = redis_client

    async def create_stream(self, name: str) -> None:
        logger.info("Creating stream", name=name)

    async def add(self, stream: str, data: dict) -> str:
        logger.debug("Adding to stream", stream=stream)
        return "0-0"

    async def read(self, stream: str, count: int = 10) -> list[dict]:
        return []

    async def consumer_group(self, stream: str, group: str) -> None:
        logger.info("Creating consumer group", stream=stream, group=group)
