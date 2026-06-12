from __future__ import annotations

import structlog

logger = structlog.get_logger()


class SSEManager:
    def __init__(self):
        self._subscribers: dict[str, list] = {}

    async def subscribe(self, channel: str, subscriber) -> None:
        if channel not in self._subscribers:
            self._subscribers[channel] = []
        self._subscribers[channel].append(subscriber)

    async def publish(self, channel: str, event: dict) -> None:
        logger.debug("Publishing SSE event", channel=channel)

    async def unsubscribe(self, channel: str, subscriber) -> None:
        subs = self._subscribers.get(channel, [])
        if subscriber in subs:
            subs.remove(subscriber)
