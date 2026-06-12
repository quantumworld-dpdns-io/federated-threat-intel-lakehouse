from __future__ import annotations

import structlog

logger = structlog.get_logger()


class WASMModuleLoader:
    def __init__(self):
        self._modules: dict[str, object] = {}

    def load_module(self, name: str, path: str) -> None:
        logger.info("Loading WASM module", name=name, path=path)
        self._modules[name] = {"path": path, "loaded": True}

    def call_function(self, module: str, function: str, args: list) -> dict:
        logger.debug("Calling WASM function", module=module, function=function)
        return {"result": None, "module": module, "function": function}

    def list_modules(self) -> list[str]:
        return list(self._modules.keys())
