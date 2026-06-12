from __future__ import annotations

import structlog

logger = structlog.get_logger()


class AgentOrchestrator:
    def __init__(self):
        self._agents: dict[str, object] = {}
        self._task_queue: list[dict] = []

    def register_agent(self, name: str, agent: object) -> None:
        self._agents[name] = agent
        logger.info("Registered agent", name=name)

    async def execute_task(self, task: dict) -> dict:
        agent_name = task.get("agent", "default")
        agent = self._agents.get(agent_name)
        if agent and hasattr(agent, "execute"):
            result = await agent.execute(task)
            return {"status": "completed", "result": result}
        return {"status": "no_agent", "task": task}

    def get_status(self) -> dict:
        return {"agents": list(self._agents.keys()), "pending_tasks": len(self._task_queue)}
