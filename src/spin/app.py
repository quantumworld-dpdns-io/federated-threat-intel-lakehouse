from __future__ import annotations

import structlog

logger = structlog.get_logger()


class SpinApp:
    def __init__(self, name: str):
        self._name = name
        self._components: list[dict] = []

    def add_component(self, name: str, trigger: str, source: str) -> None:
        self._components.append({"name": name, "trigger": trigger, "source": source})
        logger.info("Added Spin component", name=name)

    def generate_manifest(self) -> dict:
        return {
            "name": self._name,
            "version": "0.1.0",
            "trigger": {"type": "http", "base": "/"},
            "components": self._components,
        }

    def deploy(self) -> dict:
        logger.info("Deploying Spin app", name=self._name)
        return {"status": "deployed", "name": self._name, "components": len(self._components)}
