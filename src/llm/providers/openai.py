from __future__ import annotations

import structlog

from src.config import settings

logger = structlog.get_logger()


class OpenAIProvider:
    def __init__(self):
        self._model = settings.openai_model

    async def generate(self, prompt: str, system: str = "") -> str:
        logger.info("OpenAI generation", model=self._model)
        return f"Response to: {prompt[:100]}"

    async def chat(self, messages: list[dict]) -> str:
        return "Chat response"

    def get_model_info(self) -> dict:
        return {"provider": "openai", "model": self._model}
