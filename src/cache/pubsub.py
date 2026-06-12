from __future__ import annotations

import structlog

logger = structlog.get_logger()


class PubSubManager:
    def __init__(self, redis_client):
        self._redis = redis_client
        self._subscriptions: dict[str, list] = {}

    async def publish(self, channel: str, message: dict) -> int:
        logger.info("Publishing message", channel=channel)
        return 0

    async def subscribe(self, channel: str, callback) -> None:
        if channel not in self._subscriptions:
            self._subscriptions[channel] = []
        self._subscriptions[channel].append(callback)
        logger.info("Subscribed to channel", channel=channel)

    async def unsubscribe(self, channel: str) -> None:
        self._subscriptions.pop(channel, None)
