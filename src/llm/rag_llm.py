from __future__ import annotations

import structlog

from src.rag.pipeline import RAGPipeline

logger = structlog.get_logger()


class RAGLLM:
    def __init__(self, llm_provider, rag_pipeline: RAGPipeline | None = None):
        self._llm = llm_provider
        self._rag = rag_pipeline or RAGPipeline()

    async def query(self, question: str) -> dict:
        context = self._rag.retrieve(question)
        context_text = "\n".join(d.get("text", "") for d in context)
        prompt = f"Context:\n{context_text}\n\nQuestion: {question}\n\nAnswer:"
        answer = await self._llm.generate(prompt)
        return {"question": question, "answer": answer, "context_count": len(context)}

    async def summarize_threat(self, threat_data: dict) -> str:
        return await self._llm.generate(f"Summarize this threat: {threat_data}")
