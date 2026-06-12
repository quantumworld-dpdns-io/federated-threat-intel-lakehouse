from __future__ import annotations

import structlog

logger = structlog.get_logger()


class ThreatHunterSkill:
    def __init__(self):
        self._hypotheses: list[dict] = []

    def generate_hypothesis(self, context: dict) -> dict:
        hypothesis = {
            "id": len(self._hypotheses) + 1,
            "statement": f"Potential threat based on {context.get('data_source', 'unknown')}",
            "confidence": 0.7,
            "evidence": [],
        }
        self._hypotheses.append(hypothesis)
        return hypothesis

    def collect_evidence(self, hypothesis_id: int) -> list[dict]:
        return [{"type": "log_entry", "source": "siem", "finding": "Suspicious activity detected"}]

    def track_investigation(self, hypothesis_id: int) -> dict:
        return {"hypothesis_id": hypothesis_id, "status": "in_progress", "findings": 0}
