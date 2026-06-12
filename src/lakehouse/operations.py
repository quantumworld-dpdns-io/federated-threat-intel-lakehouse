from __future__ import annotations

import structlog

logger = structlog.get_logger()


class IcebergOperations:
    def __init__(self, catalog):
        self._catalog = catalog

    async def create_table(self, namespace: str, name: str, schema: dict) -> None:
        logger.info("Creating Iceberg table", namespace=namespace, name=name)

    async def append_records(self, table: str, records: list[dict]) -> int:
        logger.info("Appending records", table=table, count=len(records))
        return len(records)

    async def upsert_records(self, table: str, records: list[dict], key_field: str) -> int:
        logger.info("Upserting records", table=table, count=len(records), key=key_field)
        return len(records)

    async def delete_records(self, table: str, predicate: str) -> int:
        logger.info("Deleting records", table=table, predicate=predicate)
        return 0

    async def time_travel_snapshot(self, table: str, snapshot_id: int) -> list[dict]:
        logger.info("Time travel query", table=table, snapshot=snapshot_id)
        return []

    async def time_travel_timestamp(self, table: str, timestamp: str) -> list[dict]:
        logger.info("Time travel query", table=table, timestamp=timestamp)
        return []

    async def add_column(self, table: str, column: str, type_: str) -> None:
        logger.info("Adding column", table=table, column=column, type=type_)

    async def rename_column(self, table: str, old: str, new: str) -> None:
        logger.info("Renaming column", table=table, old=old, new=new)

    async def compact_table(self, table: str) -> None:
        logger.info("Compacting table", table=table)

    async def expire_snapshots(self, table: str, older_than: str) -> None:
        logger.info("Expiring snapshots", table=table, older_than=older_than)

    async def list_snapshots(self, table: str) -> list[dict]:
        return []
