from __future__ import annotations

import structlog

from src.rag.embeddings import EmbeddingProvider

logger = structlog.get_logger()


class RAGPipeline:
    def __init__(self):
        self._embedder = EmbeddingProvider()
        self._documents: list[dict] = []

    def index(self, documents: list[dict]) -> int:
        for doc in documents:
            doc["embedding"] = self._embedder.embed(doc.get("text", ""))
            self._documents.append(doc)
        return len(documents)

    def retrieve(self, query: str, top_k: int = 5) -> list[dict]:
        query_emb = self._embedder.embed(query)
        scored = []
        for doc in self._documents:
            doc_emb = doc.get("embedding", [])
            score = sum(a * b for a, b in zip(query_emb, doc_emb)) if doc_emb else 0
            scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for _, doc in scored[:top_k]]

    def query(self, question: str, top_k: int = 5) -> dict:
        context = self.retrieve(question, top_k)
        return {"question": question, "context": [c.get("text", "") for c in context], "answer": "Generated answer based on context"}
