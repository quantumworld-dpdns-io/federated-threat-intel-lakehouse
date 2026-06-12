from __future__ import annotations

import structlog

logger = structlog.get_logger()


class WebSocketManager:
    def __init__(self):
        self._connections: dict[str, list] = {}

    async def connect(self, client_id: str, websocket) -> None:
        if client_id not in self._connections:
            self._connections[client_id] = []
        self._connections[client_id].append(websocket)
        logger.info("WebSocket connected", client_id=client_id)

    async def disconnect(self, client_id: str) -> None:
        self._connections.pop(client_id, None)

    async def broadcast(self, channel: str, message: dict) -> None:
        logger.debug("Broadcasting message", channel=channel)

    async def send_to(self, client_id: str, message: dict) -> None:
        conns = self._connections.get(client_id, [])
        logger.debug("Sending to client", client_id=client_id, connections=len(conns))
