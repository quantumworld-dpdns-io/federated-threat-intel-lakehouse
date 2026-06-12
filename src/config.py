from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = "federated-threat-intel-lakehouse"
    app_version: str = "0.1.0"
    app_env: str = "development"
    app_debug: bool = True
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    app_secret_key: str = "change-me-in-production"
    app_cors_origins: list[str] = ["http://localhost:3000", "http://localhost:8080"]

    # Authentication
    jwt_secret_key: str = "change-me-jwt-secret"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 30
    jwt_refresh_token_expire_days: int = 7

    # Iceberg
    iceberg_catalog_type: str = "rest"
    iceberg_catalog_uri: str = "http://localhost:8181"
    iceberg_catalog_warehouse: str = "s3://threat-intel-lakehouse/warehouse"
    iceberg_s3_endpoint: str = "http://localhost:9000"
    iceberg_s3_access_key: str = "minioadmin"
    iceberg_s3_secret_key: str = "minioadmin"

    # Trino
    trino_host: str = "localhost"
    trino_port: int = 8080
    trino_catalog: str = "iceberg"
    trino_schema: str = "threat_intel"

    # DuckDB
    duckdb_path: str = "local.duckdb"

    # Redis/DragonflyDB
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0
    redis_password: str = ""
    redis_url: str = "redis://localhost:6379/0"

    # Chroma
    chroma_host: str = "localhost"
    chroma_port: int = 8500
    chroma_collection: str = "threat_intel"

    # Milvus
    milvus_host: str = "localhost"
    milvus_port: int = 19530
    milvus_collection: str = "threat_intel"

    # Weaviate
    weaviate_host: str = "localhost"
    weaviate_port: int = 8080
    weaviate_url: str = "http://localhost:8080"

    # Qdrant
    qdrant_host: str = "localhost"
    qdrant_port: int = 6333
    qdrant_url: str = "http://localhost:6333"

    # Ollama
    ollama_host: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"

    # OpenAI
    openai_api_key: str = ""
    openai_model: str = "gpt-4o"

    # Anthropic
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-3-opus-20240229"

    # IBM Quantum
    ibm_quantum_token: str = ""
    ibm_quantum_backend: str = "ibm_brisbane"

    # PQC
    pqc_enabled: bool = True
    pqc_default_algorithm: str = "CRYSTALS-Kyber-768"

    # Observability
    otel_enabled: bool = True
    otel_exporter_otlp_endpoint: str = "http://localhost:4317"
    otel_service_name: str = "federated-threat-intel-lakehouse"

    # Federated Learning
    fl_num_rounds: int = 10
    fl_min_clients: int = 3
    fl_fraction_fit: float = 0.5
    fl_strategy: str = "fedavg"
    fl_privacy_epsilon: float = 8.0
    fl_privacy_delta: float = 1e-5
    fl_gradient_clip: float = 1.0

    # S3
    s3_endpoint: str = "http://localhost:9000"
    s3_access_key: str = "minioadmin"
    s3_secret_key: str = "minioadmin"
    s3_bucket: str = "threat-intel-lakehouse"


settings = Settings()
