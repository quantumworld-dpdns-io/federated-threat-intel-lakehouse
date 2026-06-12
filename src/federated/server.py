from __future__ import annotations

import structlog

from src.federated.config import FederatedConfig

logger = structlog.get_logger()


class FederatedServer:
    def __init__(self, config: FederatedConfig | None = None):
        self._config = config or FederatedConfig()
        self._round = 0

    async def start(self) -> None:
        logger.info(
            "Starting federated server",
            strategy=self._config.strategy,
            rounds=self._config.num_rounds,
            min_clients=self._config.min_clients,
        )

    async def run_round(self) -> dict:
        self._round += 1
        logger.info("Running federated round", round=self._round)
        return {
            "round": self._round,
            "status": "completed",
            "loss": 0.5,
            "accuracy": 0.85,
            "participants": [],
        }

    async def aggregate(self, updates: list[dict]) -> dict:
        logger.info("Aggregating model updates", count=len(updates))
        return {"aggregated": True, "num_updates": len(updates)}

    async def stop(self) -> None:
        logger.info("Stopping federated server")
