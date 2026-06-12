from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID


class StorageBackend(ABC):
    @abstractmethod
    async def initialize(self) -> None: ...

    @abstractmethod
    async def create_table(self, name: str, schema: dict) -> None: ...

    @abstractmethod
    async def insert(self, table: str, records: list[dict]) -> None: ...

    @abstractmethod
    async def query(self, sql: str) -> list[dict]: ...

    @abstractmethod
    async def get_by_id(self, table: str, record_id: UUID) -> dict | None: ...

    @abstractmethod
    async def delete(self, table: str, record_id: UUID) -> bool: ...

    @abstractmethod
    async def count(self, table: str) -> int: ...

    @abstractmethod
    async def health_check(self) -> bool: ...
