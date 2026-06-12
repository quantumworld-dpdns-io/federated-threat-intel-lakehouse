*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    OperatingSystem

Suite Setup    Initialize Security Test Suite
Suite Teardown    Cleanup Security Test Suite

*** Variables ***
${BASE_URL}    http://localhost:8000
${API_BASE}    ${BASE_URL}/api/v1
${ZAP_URL}    http://localhost:8090

*** Keywords ***
Initialize Security Test Suite
    Log    Initializing OWASP Top 10 security test suite
    Create Session    api    ${BASE_URL}    verify=false

Cleanup Security Test Suite
    Log    Cleaning up security test suite
    Delete All Sessions
