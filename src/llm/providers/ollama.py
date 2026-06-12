from __future__ import annotations

import structlog

from src.config import settings

logger = structlog.get_logger()


class OllamaProvider:
    def __init__(self):
        self._model = settings.ollama_model
        self._host = settings.ollama_host

    async def generate(self, prompt: str, system: str = "") -> str:
        logger.info("Ollama generation", model=self._model)
        return f"Local response to: {prompt[:100]}"

    async def chat(self, messages: list[dict]) -> str:
        return "Local chat response"

    def get_model_info(self) -> dict:
        return {"provider": "ollama", "model": self._model, "host": self._host}
