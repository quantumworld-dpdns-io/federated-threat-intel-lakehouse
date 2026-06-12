# Deployment Guide

## Local Development

```bash
# Clone and install
git clone https://github.com/quantumworld-dpdns-io/federated-threat-intel-lakehouse.git
cd federated-threat-intel-lakehouse
make install

# Start services
make docker-up

# Run API
make dev
```

## Docker Compose Services

| Service | Port | Description |
|---------|------|-------------|
| api | 8000 | FastAPI backend |
| dragonfly | 6379 | Redis-compatible cache |
| minio | 9000/9001 | S3-compatible storage |
| trino | 8080 | Query federation |
| chroma | 8500 | Vector search (dev) |
| phoenix | 6006 | Observability |
| ollama | 11434 | Local LLM |

## Production Deployment

```bash
# Build images
docker build -f Dockerfile.python -t ftil-api .
docker build -f Dockerfile.frontend -t ftil-frontend ./frontend

# Deploy with production overrides
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

## Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ftil-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ftil-api
  template:
    spec:
      containers:
      - name: api
        image: ghcr.io/quantumworld-dpdns-io/federated-threat-intel-lakehouse:latest
        ports:
        - containerPort: 8000
```
