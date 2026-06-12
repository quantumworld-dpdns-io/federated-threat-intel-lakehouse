# Federated Learning

## Overview

Privacy-preserving threat intelligence sharing across organizations using federated learning.

## Strategies

| Strategy | Description |
|----------|-------------|
| FedAvg | Federated Averaging (default) |
| FedProx | Proximal term for heterogeneity |
| FedNova | Normalized averaging |
| FedAdam | Adaptive learning rate |
| FedYogi | Adaptive variance reduction |

## Privacy

- **Differential Privacy**: Gaussian noise injection with configurable ε, δ
- **Secure Aggregation**: Secret sharing for model update privacy
- **Gradient Clipping**: Bounded sensitivity

## Usage

```python
from src.federated.orchestrator import FLClusterOrchestrator
from src.federated.config import FederatedConfig

config = FederatedConfig(num_rounds=10, min_clients=3)
orchestrator = FLClusterOrchestrator(config)

await orchestrator.register_client("node-1")
results = await orchestrator.run_training()
```
