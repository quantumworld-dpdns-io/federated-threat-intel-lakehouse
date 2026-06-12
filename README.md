# Federated Threat Intelligence Lakehouse

> Privacy-preserving CTI contribution for SMEs using federated learning, Apache Iceberg/Trino, and quantum computing.

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    Federated Threat Intel Lakehouse             │
├─────────────┬──────────────┬──────────────┬────────────────────┤
│   Frontend  │   API Layer  │  FL Engine   │  Quantum Module    │
│  (Next.js)  │  (FastAPI)   │  (Flower)    │  (Qiskit/CUDA-Q)  │
├─────────────┴──────┬───────┴──────┬───────┴────────────────────┤
│   Data Lakehouse   │   Vector DB  │      Redis/Cache            │
│  (Iceberg/Trino)   │  (Chroma/    │    (DragonflyDB)            │
│                    │   Milvus)    │                             │
├────────────────────┴──────────────┴─────────────────────────────┤
│                    Object Storage (MinIO/S3)                     │
└─────────────────────────────────────────────────────────────────┘
```

## Quick Start

```bash
git clone https://github.com/quantumworld-dpdns-io/federated-threat-intel-lakehouse.git
cd federated-threat-intel-lakehouse
cp .env.example .env
make install
make docker-up
make dev
```

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Primary Language | Python 3.12+ |
| Performance Core | Rust |
| API Layer | FastAPI |
| Frontend | Next.js 14 |
| Data Lakehouse | Apache Iceberg + Trino + DataFusion |
| Vector DB | Chroma (dev) / Milvus (prod) |
| Cache | DragonflyDB (Redis-compatible) |
| Federated Learning | Flower + NVIDIA FLARE |
| Quantum | Qiskit + CUDA-Q + PQC + ZKP |
| Security Testing | RobotFramework + OWASP ZAP |
| CI/CD | GitHub Actions |
| Observability | OpenTelemetry + Arize Phoenix |

## Features

### Data Lakehouse
- Apache Iceberg for ACID transactions and time travel
- Trino for federated cross-source queries
- DataFusion for high-performance analytics
- Arrow/Polars for columnar data processing

### Vector Database & RAG
- Chroma for development vector search
- Milvus for production vector search
- Weaviate and Qdrant support
- End-to-end RAG pipeline for threat intelligence

### Federated Learning
- Flower (flwr) for federated learning orchestration
- NVIDIA FLARE for enterprise FL
- Differential privacy and secure aggregation
- FedAvg, FedProx, FedNova, FedAdam strategies

### Quantum Computing
- Qiskit for quantum circuit execution
- NVIDIA CUDA-Q for GPU-accelerated simulation
- Post-quantum cryptography (CRYSTALS-Kyber, Dilithium)
- Zero-knowledge proofs (Noir, RISC Zero)
- Quantum key distribution (BB84)
- Quantum random number generation

### Security Testing
- OWASP Top 10 RobotFramework test suites
- OWASP ZAP automated scanning
- CI/CD security gates
- Nightly security scans

### AI Agents & LLM
- MCP (Model Context Protocol) server
- OpenAI, Anthropic, Ollama integration
- RAG-augmented LLM for threat analysis
- Agent skills for threat hunting, IoC analysis

### Real-Time Processing
- WebSocket streaming for live updates
- Redis pub/sub for alerts
- Redis Streams for event sourcing
- Kafka integration for high-volume ingestion

## Project Structure

```
.
├── src/                    # Python source code
│   ├── api/               # FastAPI application
│   ├── models/            # Pydantic data models
│   ├── storage/           # Storage backends
│   ├── lakehouse/         # Iceberg/Trino/DataFusion
│   ├── cache/             # Redis/DragonflyDB
│   ├── federated/         # Federated learning
│   ├── quantum/           # Quantum computing
│   ├── rag/               # RAG pipeline
│   ├── mcp/               # MCP server
│   ├── agents/            # AI agents
│   ├── llm/               # LLM providers
│   ├── observability/     # Tracing & metrics
│   ├── streaming/         # WebSocket/SSE/Kafka
│   ├── wasm/              # WebAssembly modules
│   └── spin/              # Fermyon Spin
├── crates/                 # Rust source code
│   ├── core/              # Shared types
│   ├── query-engine/      # DataFusion engine
│   └── wasm-modules/      # WASM parsers
├── frontend/               # Next.js dashboard
├── tests/                  # Test suites
│   ├── unit/              # pytest unit tests
│   ├── integration/       # Integration tests
│   └── robot/             # RobotFramework tests
│       └── security/      # OWASP Top 10 tests
├── docs/                   # Documentation
└── .github/workflows/      # CI/CD pipelines
```

## Testing

```bash
# Unit tests
make test

# Integration tests
make test-integration

# Security tests (RobotFramework)
make test-security

# All tests
make test-verbose
```

## CI/CD

- **CI**: Lint, typecheck, test, build (Python + Rust + Next.js)
- **Security**: OWASP Top 10 tests, ZAP scans, dependency audit
- **Release**: Semantic versioning, PyPI/crates.io/npm publishing
- **Docker**: Multi-arch builds, GHCR/Docker Hub publishing
- **Scheduled**: Nightly dependency audit, weekly full scan, monthly PQC assessment

## Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md).

## License

[MIT](LICENSE)
