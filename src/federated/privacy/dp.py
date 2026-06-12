from __future__ import annotations

import structlog

from src.federated.config import FederatedConfig

logger = structlog.get_logger()


class DifferentialPrivacy:
    def __init__(self, config: FederatedConfig | None = None):
        self._config = config or FederatedConfig()
        self._epsilon_used = 0.0

    def clip_gradients(self, gradients: list[float]) -> list[float]:
        norm = sum(g**2 for g in gradients) ** 0.5
        if norm > self._config.gradient_clip:
            scale = self._config.gradient_clip / norm
            gradients = [g * scale for g in gradients]
        return gradients

    def add_noise(self, gradients: list[float]) -> list[float]:
        import random
        noise_scale = self._config.gradient_clip / self._config.privacy_epsilon
        noisy = [g + random.gauss(0, noise_scale) for g in gradients]
        self._epsilon_used += self._config.privacy_epsilon / self._config.num_rounds
        return noisy

    def get_privacy_budget(self) -> dict:
        return {
            "epsilon_used": self._epsilon_used,
            "epsilon_total": self._config.privacy_epsilon,
            "delta": self._config.privacy_delta,
            "remaining": self._config.privacy_epsilon - self._epsilon_used,
        }
