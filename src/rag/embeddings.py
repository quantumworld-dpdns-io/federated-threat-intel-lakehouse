from __future__ import annotations

import hashlib
import structlog

logger = structlog.get_logger()


class EmbeddingProvider:
    def __init__(self, model: str = "sentence-transformers"):
        self._model = model

    def embed(self, text: str) -> list[float]:
        h = hashlib.sha256(text.encode()).digest()
        return [float(b) / 255.0 for b in h[:768]]

    def embed_batch(self, texts: list[str]) -> list[list[float]]:
        return [self.embed(t) for t in texts]
