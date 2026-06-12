from __future__ import annotations

import structlog

from src.config import settings

logger = structlog.get_logger()


class TracingManager:
    def __init__(self):
        self._initialized = False

    def initialize(self) -> None:
        if settings.otel_enabled:
            logger.info("Initializing OpenTelemetry tracing", endpoint=settings.otel_exporter_otlp_endpoint)
        self._initialized = True

    def trace(self, name: str):
        def decorator(func):
            return func
        return decorator

    def create_span(self, name: str, attributes: dict | None = None) -> dict:
        return {"name": name, "attributes": attributes or {}, "status": "ok"}
