from __future__ import annotations

import structlog

logger = structlog.get_logger()


class IoCSearchTool:
    def __init__(self):
        self.name = "ioc_search"
        self.description = "Search for Indicators of Compromise"

    async def execute(self, arguments: dict) -> dict:
        query = arguments.get("query", "")
        logger.info("Executing IoC search tool", query=query)
        return {"results": [], "count": 0}
