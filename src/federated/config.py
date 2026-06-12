from __future__ import annotations

from pydantic import BaseModel, Field

from src.config import settings


class FederatedConfig(BaseModel):
    num_rounds: int = Field(default_factory=lambda: settings.fl_num_rounds)
    min_clients: int = Field(default_factory=lambda: settings.fl_min_clients)
    fraction_fit: float = Field(default_factory=lambda: settings.fl_fraction_fit)
    strategy: str = Field(default_factory=lambda: settings.fl_strategy)
    privacy_epsilon: float = Field(default_factory=lambda: settings.fl_privacy_epsilon)
    privacy_delta: float = Field(default_factory=lambda: settings.fl_privacy_delta)
    gradient_clip: float = Field(default_factory=lambda: settings.fl_gradient_clip)
    local_epochs: int = 5
    batch_size: int = 32
    learning_rate: float = 0.01
    weight_decay: float = 1e-4
    secure_aggregation: bool = True
    compression: bool = False
