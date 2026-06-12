from __future__ import annotations

import structlog

from src.federated.config import FederatedConfig
from src.federated.server import FederatedServer

logger = structlog.get_logger()


class FLClusterOrchestrator:
    def __init__(self, config: FederatedConfig | None = None):
        self._config = config or FederatedConfig()
        self._server = FederatedServer(self._config)
        self._clients: list[str] = []
        self._round_results: list[dict] = []

    async def register_client(self, client_id: str) -> None:
        self._clients.append(client_id)
        logger.info("Registered FL client", client_id=client_id, total=len(self._clients))

    async def run_training(self) -> list[dict]:
        await self._server.start()
        for round_num in range(self._config.num_rounds):
            result = await self._server.run_round()
            self._round_results.append(result)
            logger.info(
                "Round completed",
                round=round_num + 1,
                loss=result.get("loss"),
                accuracy=result.get("accuracy"),
            )
        await self._server.stop()
        return self._round_results

    async def get_status(self) -> dict:
        return {
            "clients": len(self._clients),
            "rounds_completed": len(self._round_results),
            "config": self._config.model_dump(),
        }
