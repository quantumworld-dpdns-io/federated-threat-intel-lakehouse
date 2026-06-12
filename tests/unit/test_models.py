import pytest
from uuid import uuid4

from src.models.ioc import IoC, IoCCreate, IoCResponse
from src.models.campaign import Campaign, CampaignCreate
from src.models.vulnerability import Vulnerability, VulnerabilityCreate
from src.models.enums import IoCType, Severity, Tlp, Confidence, CampaignStatus


class TestIoCModel:
    def test_create_ioc(self):
        ioc = IoCCreate(
            ioc_type=IoCType.IP_ADDRESS,
            value="192.168.1.1",
            source="test",
        )
        assert ioc.ioc_type == IoCType.IP_ADDRESS
        assert ioc.value == "192.168.1.1"

    def test_ioc_response(self):
        ioc = IoCResponse(
            ioc_type=IoCType.DOMAIN,
            value="evil.com",
            source="test",
            severity=Severity.HIGH,
        )
        assert ioc.id is not None
        assert ioc.severity == Severity.HIGH

    def test_ioc_default_values(self):
        ioc = IoCCreate(
            ioc_type=IoCType.CVE,
            value="CVE-2024-1234",
            source="test",
        )
        assert ioc.severity == Severity.MEDIUM
        assert ioc.tlp == Tlp.GREEN
        assert ioc.tags == []

    def test_ioc_validation_empty_value(self):
        with pytest.raises(Exception):
            IoCCreate(
                ioc_type=IoCType.IP_ADDRESS,
                value="",
                source="test",
            )


class TestCampaignModel:
    def test_create_campaign(self):
        campaign = CampaignCreate(
            name="Test Campaign",
            description="A test campaign",
        )
        assert campaign.name == "Test Campaign"
        assert campaign.status == CampaignStatus.ACTIVE

    def test_campaign_response(self):
        campaign = Campaign(
            name="APT-29",
            description="Test",
            severity=Severity.CRITICAL,
        )
        assert campaign.id is not None


class TestVulnerabilityModel:
    def test_create_vulnerability(self):
        vuln = VulnerabilityCreate(
            cve_id="CVE-2024-1234",
            description="Test vulnerability",
        )
        assert vuln.cve_id == "CVE-2024-1234"
        assert vuln.cvss_score is None

    def test_invalid_cve_format(self):
        with pytest.raises(Exception):
            VulnerabilityCreate(
                cve_id="INVALID",
                description="Test",
            )
