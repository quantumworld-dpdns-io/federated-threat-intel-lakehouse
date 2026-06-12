from __future__ import annotations

import structlog

logger = structlog.get_logger()


class MCPServer:
    def __init__(self, name: str = "ftil-mcp-server"):
        self._name = name
        self._tools: list[dict] = []
        self._resources: list[dict] = []

    def register_tool(self, name: str, description: str, parameters: dict) -> None:
        self._tools.append({"name": name, "description": description, "parameters": parameters})
        logger.info("Registered MCP tool", name=name)

    def register_resource(self, name: str, description: str, uri: str) -> None:
        self._resources.append({"name": name, "description": description, "uri": uri})
        logger.info("Registered MCP resource", name=name)

    async def handle_request(self, request: dict) -> dict:
        method = request.get("method", "")
        if method == "tools/list":
            return {"tools": self._tools}
        elif method == "resources/list":
            return {"resources": self._resources}
        elif method == "tools/call":
            tool_name = request.get("params", {}).get("name", "")
            return await self.call_tool(tool_name, request.get("params", {}).get("arguments", {}))
        return {"error": "Unknown method"}

    async def call_tool(self, name: str, arguments: dict) -> dict:
        logger.info("Calling MCP tool", name=name)
        return {"content": [{"type": "text", "text": f"Result from {name}"}]}

    def get_server_info(self) -> dict:
        return {"name": self._name, "tools": len(self._tools), "resources": len(self._resources)}
