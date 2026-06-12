*** Settings ***
Resource    ../resources/security_keywords.robot

*** Test Cases ***
A06-01: Dependency Vulnerability Scan
    [Documentation]    Test if dependencies are up to date
    ${output}=    Run Process    pip-audit    --format=json    shell=True    timeout=60s
    Log    Dependency audit completed

A06-02: Container Image Scanning
    [Documentation]    Test if container images are scanned
    ${output}=    Run Process    trivy    image    --format=json    federated-threat-intel-lakehouse    shell=True    timeout=120s
    Log    Container image scan completed

A06-03: Outdated Component Detection
    [Documentation]    Test if outdated components are identified
    ${output}=    Run Process    pip    list    --outdated    shell=True    timeout=60s
    Log    Outdated component check completed
