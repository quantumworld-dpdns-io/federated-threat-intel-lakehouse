# Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Federated Threat Intel Lakehouse             │
├─────────────┬──────────────┬──────────────┬────────────────────┤
│   Frontend  │   API Layer  │  FL Engine   │  Quantum Module    │
│  (Next.js)  │  (FastAPI)   │  (Flower)    │  (Qiskit/CUDA-Q)  │
├─────────────┴──────┬───────┴──────┬───────┴────────────────────┤
│                    │              │                             │
│   Data Lakehouse   │   Vector DB  │      Redis/Cache            │
│  (Iceberg/Trino)   │  (Chroma/    │    (DragonflyDB)            │
│                    │   Milvus)    │                             │
├────────────────────┴──────────────┴─────────────────────────────┤
│                    Object Storage (MinIO/S3)                     │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow

1. **Ingestion**: IoCs arrive via API, STIX import, or federated nodes
2. **Storage**: Data persisted in Iceberg tables on object storage
3. **Query**: Trino federates across Iceberg, DuckDB, and external sources
4. **Analysis**: DataFusion UDFs perform threat scoring and correlation
5. **Vectorization**: Threat descriptions embedded and stored in Chroma/Milvus
6. **FL Training**: Federated learning trains threat classifiers across nodes
7. **Quantum Enhancement**: Quantum circuits improve classification accuracy
8. **API Delivery**: FastAPI serves results with MCP integration

## Security Model

- JWT + API key authentication
- Differential privacy for federated learning
- Post-quantum cryptography for data protection
- OWASP Top 10 security testing via RobotFramework
- Zero-knowledge proofs for data provenance
