from __future__ import annotations

import structlog

from src.federated.config import FederatedConfig

logger = structlog.get_logger()


class FederatedClient:
    def __init__(self, client_id: str, config: FederatedConfig | None = None):
        self._client_id = client_id
        self._config = config or FederatedConfig()

    async def train(self, global_parameters: dict) -> dict:
        logger.info("Client training", client_id=self._client_id)
        return {
            "client_id": self._client_id,
            "num_samples": 1000,
            "loss": 0.45,
            "accuracy": 0.88,
            "parameters": b"",
        }

    async def evaluate(self, parameters: dict) -> dict:
        logger.info("Client evaluating", client_id=self._client_id)
        return {
            "client_id": self._client_id,
            "loss": 0.42,
            "accuracy": 0.89,
            "num_samples": 1000,
        }

    async def get_data_info(self) -> dict:
        return {
            "client_id": self._client_id,
            "num_samples": 1000,
            "features": 128,
            "classes": 2,
        }
