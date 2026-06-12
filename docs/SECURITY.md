# Security Testing Guide

## OWASP Top 10 Coverage

| Category | Test File | Status |
|----------|-----------|--------|
| A01: Broken Access Control | `owasp_a01_broken_access_control.robot` | Implemented |
| A02: Cryptographic Failures | `owasp_a02_cryptographic_failures.robot` | Implemented |
| A03: Injection | `owasp_a03_injection.robot` | Implemented |
| A04: Insecure Design | `owasp_a04_insecure_design.robot` | Implemented |
| A05: Security Misconfiguration | `owasp_a05_security_misconfiguration.robot` | Implemented |
| A06: Vulnerable Components | `owasp_a06_vulnerable_components.robot` | Implemented |
| A07: Auth Failures | `owasp_a07_auth_failures.robot` | Implemented |
| A08: Data Integrity | `owasp_a08_data_integrity.robot` | Implemented |
| A09: Logging & Monitoring | `owasp_a09_logging_monitoring.robot` | Implemented |
| A10: SSRF | `owasp_a10_ssrf.robot` | Implemented |

## Running Security Tests

```bash
# Run all OWASP tests
make test-security

# Run with RobotFramework directly
python -m robot --loglevel DEBUG tests/robot/security/

# Run specific OWASP category
python -m robot tests/robot/security/owasp_a03_injection.robot
```

## ZAP Integration

```bash
# Start ZAP
docker run -u zap -p 8090:8090 -p 8080:8080 ghcr.io/zaproxy/zaproxy:stable zap.sh -daemon

# Run ZAP scan
python -m robot tests/robot/security/zap/
```

## CI/CD Integration

Security tests run automatically:
- On every push to `main`
- On every pull request
- Nightly full scan (2 AM UTC)
- Weekly comprehensive audit
- Monthly PQC readiness assessment
