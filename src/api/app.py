from __future__ import annotations

from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src import __version__
from src.config import settings

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(
        "Starting application",
        version=__version__,
        env=settings.app_env,
    )
    yield
    logger.info("Shutting down application")


def create_app() -> FastAPI:
    app = FastAPI(
        title="Federated Threat Intelligence Lakehouse",
        description="Privacy-preserving CTI contribution using federated learning and Apache Iceberg/Trino",
        version=__version__,
        docs_url="/docs" if settings.app_debug else None,
        redoc_url="/redoc" if settings.app_debug else None,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.app_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.error("Unhandled exception", error=str(exc), path=request.url.path)
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )

    from src.api.routers import (
        analytics,
        campaigns,
        enrichment,
        export,
        federation,
        health,
        iocs,
        import_,
        quantum,
        stream,
        vulnerabilities,
    )

    app.include_router(health.router, prefix="/api/v1", tags=["health"])
    app.include_router(iocs.router, prefix="/api/v1/iocs", tags=["iocs"])
    app.include_router(campaigns.router, prefix="/api/v1/campaigns", tags=["campaigns"])
    app.include_router(vulnerabilities.router, prefix="/api/v1/vulnerabilities", tags=["vulnerabilities"])
    app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])
    app.include_router(enrichment.router, prefix="/api/v1/enrichment", tags=["enrichment"])
    app.include_router(federation.router, prefix="/api/v1/federation", tags=["federation"])
    app.include_router(quantum.router, prefix="/api/v1/quantum", tags=["quantum"])
    app.include_router(export.router, prefix="/api/v1/export", tags=["export"])
    app.include_router(import_.router, prefix="/api/v1/import", tags=["import"])
    app.include_router(stream.router, prefix="/api/v1/stream", tags=["stream"])

    return app
