import pytest
from fastapi.testclient import TestClient

from src.api.app import create_app
from src.models.enums import Confidence, IoCType, Severity, Tlp


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def client(app):
    return TestClient(app)


@pytest.fixture
def sample_ioc_data():
    return {
        "ioc_type": IoCType.IP_ADDRESS.value,
        "value": "192.168.1.100",
        "severity": Severity.HIGH.value,
        "confidence": Confidence.HIGH.value,
        "tlp": Tlp.AMBER.value,
        "tags": ["malware", "c2"],
        "source": "threat-intel-feed",
        "description": "Known C2 server IP",
    }


@pytest.fixture
def sample_campaign_data():
    return {
        "name": "APT-29 Campaign",
        "description": "State-sponsored campaign targeting government agencies",
        "severity": Severity.CRITICAL.value,
        "status": "active",
        "tags": ["apt29", "state-sponsored"],
    }


@pytest.fixture
def sample_vuln_data():
    return {
        "cve_id": "CVE-2024-12345",
        "description": "Critical RCE vulnerability in vendor product",
        "severity": Severity.CRITICAL.value,
        "cvss_score": 9.8,
        "exploit_available": True,
        "patch_available": False,
    }
