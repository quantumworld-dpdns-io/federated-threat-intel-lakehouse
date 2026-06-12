*** Settings ***
Resource    ../resources/security_keywords.robot

*** Test Cases ***
A10-01: SSRF via URL Fetch
    [Documentation]    Test if server-side request forgery is possible via URL
    ${payload}=    Set Variable    http://169.254.169.254/latest/meta-data/
    ${resp}=    Make API Request    POST    /api/v1/enrichment/test-ioc-id    data={"url": "${payload}"}
    Should Not Contain    ${resp.text}    ami-id
    Log    SSRF URL fetch test completed

A10-02: SSRF via IoC Enrichment
    [Documentation]    Test SSRF via enrichment endpoints
    ${payload}=    Set Variable    http://localhost:8000/api/v1/internal/admin
    ${resp}=    Make API Request    POST    /api/v1/enrichment/test-ioc-id    data={"provider": "custom", "url": "${payload}"}
    Log    SSRF enrichment test completed

A10-03: SSRF via Import
    [Documentation]    Test SSRF via import endpoints
    ${payload}=    Set Variable    http://169.254.169.254/latest/meta-data/iam/security-credentials/
    ${resp}=    Make API Request    POST    /api/v1/import/stix    data={"url": "${payload}"}
    Should Not Contain    ${resp.text}    AccessKey
    Log    SSRF import test completed
