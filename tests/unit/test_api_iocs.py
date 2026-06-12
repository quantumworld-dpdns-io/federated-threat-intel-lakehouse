import pytest


class TestIoCAPI:
    def test_create_ioc(self, client, sample_ioc_data):
        response = client.post("/api/v1/iocs", json=sample_ioc_data)
        assert response.status_code == 201
        data = response.json()
        assert data["ioc_type"] == "ip_address"
        assert data["value"] == "192.168.1.100"

    def test_list_iocs(self, client):
        response = client.get("/api/v1/iocs")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_ioc_not_found(self, client):
        response = client.get("/api/v1/iocs/00000000-0000-0000-0000-000000000000")
        assert response.status_code == 404

    def test_bulk_create(self, client, sample_ioc_data):
        data = [sample_ioc_data, {**sample_ioc_data, "value": "10.0.0.1"}]
        response = client.post("/api/v1/iocs/bulk", json=data)
        assert response.status_code == 201
        assert len(response.json()) == 2

    def test_search_iocs(self, client, sample_ioc_data):
        client.post("/api/v1/iocs", json=sample_ioc_data)
        response = client.post("/api/v1/iocs/search?query=192.168")
        assert response.status_code == 200


class TestCampaignAPI:
    def test_create_campaign(self, client, sample_campaign_data):
        response = client.post("/api/v1/campaigns", json=sample_campaign_data)
        assert response.status_code == 201
        assert response.json()["name"] == "APT-29 Campaign"

    def test_list_campaigns(self, client):
        response = client.get("/api/v1/campaigns")
        assert response.status_code == 200


class TestVulnerabilityAPI:
    def test_create_vulnerability(self, client, sample_vuln_data):
        response = client.post("/api/v1/vulnerabilities", json=sample_vuln_data)
        assert response.status_code == 201
        assert response.json()["cve_id"] == "CVE-2024-12345"


class TestHealthAPI:
    def test_health(self, client):
        response = client.get("/api/v1/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"

    def test_readiness(self, client):
        response = client.get("/api/v1/ready")
        assert response.status_code == 200

    def test_liveness(self, client):
        response = client.get("/api/v1/live")
        assert response.status_code == 200
