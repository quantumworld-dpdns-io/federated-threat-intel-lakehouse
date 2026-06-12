import pytest
from fastapi.testclient import TestClient

from src.api.app import create_app


@pytest.fixture
def client():
    return TestClient(create_app())


class TestIoCIntegration:
    def test_ioc_lifecycle(self, client):
        create_data = {
            "ioc_type": "ip_address",
            "value": "10.0.0.1",
            "source": "integration-test",
            "severity": "high",
        }
        resp = client.post("/api/v1/iocs", json=create_data)
        assert resp.status_code == 201
        ioc = resp.json()
        ioc_id = ioc["id"]

        resp = client.get(f"/api/v1/iocs/{ioc_id}")
        assert resp.status_code == 200
        assert resp.json()["value"] == "10.0.0.1"

        update_data = {"severity": "critical"}
        resp = client.put(f"/api/v1/iocs/{ioc_id}", json=update_data)
        assert resp.status_code == 200
        assert resp.json()["severity"] == "critical"

        resp = client.delete(f"/api/v1/iocs/{ioc_id}")
        assert resp.status_code == 204

        resp = client.get(f"/api/v1/iocs/{ioc_id}")
        assert resp.status_code == 404

    def test_campaign_lifecycle(self, client):
        create_data = {
            "name": "Integration Test Campaign",
            "description": "Testing campaign lifecycle",
            "severity": "medium",
        }
        resp = client.post("/api/v1/campaigns", json=create_data)
        assert resp.status_code == 201
        campaign_id = resp.json()["id"]

        resp = client.get(f"/api/v1/campaigns/{campaign_id}")
        assert resp.status_code == 200

        resp = client.delete(f"/api/v1/campaigns/{campaign_id}")
        assert resp.status_code == 204


class TestQuantumIntegration:
    def test_quantum_status(self, client):
        resp = client.get("/api/v1/quantum/status")
        assert resp.status_code == 200
        data = resp.json()
        assert "qiskit_available" in data
        assert "pqc_enabled" in data

    def test_circuit_creation(self, client):
        circuit_data = {
            "name": "test-circuit",
            "num_qubits": 4,
            "depth": 2,
            "backend": "statevector_simulator",
            "shots": 1024,
        }
        resp = client.post("/api/v1/quantum/circuits", json=circuit_data)
        assert resp.status_code == 201

    def test_key_generation(self, client):
        key_data = {"algorithm": "CRYSTALS-Kyber-768", "key_size": 256}
        resp = client.post("/api/v1/quantum/keys", json=key_data)
        assert resp.status_code == 201


class TestFederationIntegration:
    def test_node_registration(self, client):
        node_data = {
            "name": "test-node",
            "organization": "Test Org",
            "endpoint": "http://localhost:8001",
        }
        resp = client.post("/api/v1/federation/nodes", json=node_data)
        assert resp.status_code == 201

    def test_federation_status(self, client):
        resp = client.get("/api/v1/federation/status")
        assert resp.status_code == 200
        assert "total_nodes" in resp.json()
