from __future__ import annotations

import structlog

logger = structlog.get_logger()


class SessionCache:
    def __init__(self, redis_client):
        self._redis = redis_client
        self._prefix = "session"

    async def create_session(self, session_id: str, user_id: str, ttl: int = 1800) -> None:
        logger.info("Creating session", session_id=session_id)

    async def get_session(self, session_id: str) -> dict | None:
        return None

    async def delete_session(self, session_id: str) -> None:
        pass

    async def blacklist_token(self, token: str, ttl: int = 1800) -> None:
        logger.info("Blacklisting token")

    async def is_token_blacklisted(self, token: str) -> bool:
        return False
