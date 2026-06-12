from __future__ import annotations

import structlog

logger = structlog.get_logger()


class QuantumAnomalyDetection:
    def __init__(self, sensitivity: float = 0.8):
        self._sensitivity = sensitivity

    def detect_network_anomaly(self, traffic_features: list[float]) -> dict:
        mean = sum(traffic_features) / len(traffic_features) if traffic_features else 0
        variance = sum((x - mean) ** 2 for x in traffic_features) / len(traffic_features) if traffic_features else 0
        anomaly_score = variance ** 0.5 / (mean + 1e-10)
        return {"anomaly_score": anomaly_score, "is_anomalous": anomaly_score > self._sensitivity}

    def detect_dns_tunneling(self, dns_features: dict) -> dict:
        entropy = -sum(p * __import__("math").log2(p) for p in [0.3, 0.3, 0.2, 0.2] if p > 0)
        return {"tunneling_probability": min(entropy / 4.0, 1.0), "entropy": entropy}

    def detect_c2(self, connection_features: list[dict]) -> dict:
        suspicious = sum(1 for c in connection_features if c.get("periodic", False))
        return {"c2_probability": suspicious / max(len(connection_features), 1), "suspicious_connections": suspicious}

    def detect_lateral_movement(self, auth_events: list[dict]) -> dict:
        unique_pairs = set((e.get("src"), e.get("dst")) for e in auth_events)
        return {"lateral_movement_score": len(unique_pairs) / max(len(auth_events), 1), "unique_pairs": len(unique_pairs)}

    def detect_exfiltration(self, flow_features: list[dict]) -> dict:
        large_flows = sum(1 for f in flow_features if f.get("bytes", 0) > 1_000_000)
        return {"exfiltration_score": large_flows / max(len(flow_features), 1), "large_flows": large_flows}
