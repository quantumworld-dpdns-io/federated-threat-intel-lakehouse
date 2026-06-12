from __future__ import annotations

THREAT_INDICATOR_SCHEMA = {
    "fields": [
        {"name": "id", "type": "string", "required": True},
        {"name": "ioc_type", "type": "string", "required": True},
        {"name": "value", "type": "string", "required": True},
        {"name": "severity", "type": "string", "required": True},
        {"name": "confidence", "type": "string", "required": True},
        {"name": "tlp", "type": "string", "required": True},
        {"name": "tags", "type": "list<string>", "required": False},
        {"name": "source", "type": "string", "required": True},
        {"name": "first_seen", "type": "timestamp", "required": True},
        {"name": "last_seen", "type": "timestamp", "required": True},
        {"name": "description", "type": "string", "required": False},
        {"name": "mitre_tactics", "type": "list<string>", "required": False},
        {"name": "mitre_techniques", "type": "list<string>", "required": False},
        {"name": "campaign_id", "type": "string", "required": False},
        {"name": "threat_actor_id", "type": "string", "required": False},
    ],
    "partition_spec": [
        {"name": "severity", "transform": "identity"},
        {"name": "first_seen", "transform": "day"},
    ],
    "sort_order": [
        {"name": "first_seen", "direction": "desc"},
    ],
}

CAMPAIGN_SCHEMA = {
    "fields": [
        {"name": "id", "type": "string", "required": True},
        {"name": "name", "type": "string", "required": True},
        {"name": "description", "type": "string", "required": True},
        {"name": "severity", "type": "string", "required": True},
        {"name": "status", "type": "string", "required": True},
        {"name": "threat_actor_id", "type": "string", "required": False},
        {"name": "first_seen", "type": "timestamp", "required": True},
        {"name": "last_seen", "type": "timestamp", "required": True},
        {"name": "tags", "type": "list<string>", "required": False},
        {"name": "mitre_tactics", "type": "list<string>", "required": False},
    ],
}

THREAT_ACTOR_SCHEMA = {
    "fields": [
        {"name": "id", "type": "string", "required": True},
        {"name": "name", "type": "string", "required": True},
        {"name": "aliases", "type": "list<string>", "required": False},
        {"name": "description", "type": "string", "required": True},
        {"name": "motivation", "type": "string", "required": False},
        {"name": "sophistication", "type": "string", "required": False},
        {"name": "country", "type": "string", "required": False},
        {"name": "first_seen", "type": "timestamp", "required": True},
        {"name": "last_seen", "type": "timestamp", "required": True},
        {"name": "tags", "type": "list<string>", "required": False},
    ],
}

VULNERABILITY_SCHEMA = {
    "fields": [
        {"name": "id", "type": "string", "required": True},
        {"name": "cve_id", "type": "string", "required": True},
        {"name": "description", "type": "string", "required": True},
        {"name": "severity", "type": "string", "required": True},
        {"name": "cvss_score", "type": "double", "required": False},
        {"name": "affected_software", "type": "list<string>", "required": False},
        {"name": "exploit_available", "type": "boolean", "required": True},
        {"name": "patch_available", "type": "boolean", "required": True},
    ],
}

AUDIT_LOG_SCHEMA = {
    "fields": [
        {"name": "id", "type": "string", "required": True},
        {"name": "timestamp", "type": "timestamp", "required": True},
        {"name": "actor", "type": "string", "required": True},
        {"name": "action", "type": "string", "required": True},
        {"name": "resource_type", "type": "string", "required": True},
        {"name": "resource_id", "type": "string", "required": True},
        {"name": "details", "type": "string", "required": False},
        {"name": "ip_address", "type": "string", "required": False},
    ],
}

FEDERATED_MODEL_UPDATE_SCHEMA = {
    "fields": [
        {"name": "id", "type": "string", "required": True},
        {"name": "node_id", "type": "string", "required": True},
        {"name": "round_number", "type": "long", "required": True},
        {"name": "num_samples", "type": "long", "required": True},
        {"name": "loss", "type": "double", "required": True},
        {"name": "accuracy", "type": "double", "required": False},
        {"name": "created_at", "type": "timestamp", "required": True},
    ],
}
