from __future__ import annotations

import structlog

from src.config import settings

logger = structlog.get_logger()


class ChromaClient:
    def __init__(self):
        self._client = None
        self._initialized = False

    async def initialize(self) -> None:
        logger.info("Initializing Chroma client", host=settings.chroma_host, port=settings.chroma_port)
        self._initialized = True

    async def create_collection(self, name: str) -> None:
        logger.info("Creating Chroma collection", name=name)

    async def add(self, collection: str, documents: list[str], ids: list[str], metadatas: list[dict] | None = None) -> None:
        logger.info("Adding to Chroma", collection=collection, count=len(documents))

    async def query(self, collection: str, query: str, n_results: int = 10) -> list[dict]:
        return []

    async def delete(self, collection: str, ids: list[str]) -> None:
        pass
