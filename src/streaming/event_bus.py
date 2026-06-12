from __future__ import annotations

import structlog

logger = structlog.get_logger()


class EventBus:
    def __init__(self):
        self._handlers: dict[str, list] = {}
        self._events: list[dict] = []

    def subscribe(self, event_type: str, handler) -> None:
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    async def publish(self, event_type: str, data: dict) -> None:
        event = {"type": event_type, "data": data}
        self._events.append(event)
        handlers = self._handlers.get(event_type, [])
        for handler in handlers:
            if hasattr(handler, "__call__"):
                await handler(event)

    def get_events(self, event_type: str | None = None) -> list[dict]:
        if event_type:
            return [e for e in self._events if e["type"] == event_type]
        return self._events
