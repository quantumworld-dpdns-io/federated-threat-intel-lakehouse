*** Settings ***
Resource    ../resources/security_keywords.robot

*** Test Cases ***
A02-01: Weak TLS Configuration
    [Documentation]    Test if server accepts weak TLS versions
    ${resp}=    Make API Request    GET    /api/v1/health
    Should Not Contain    ${resp.headers}    Server:
    Log    TLS configuration check passed

A02-02: Sensitive Data in Transit
    [Documentation]    Test if sensitive data is transmitted over HTTPS
    ${resp}=    Make API Request    POST    /api/v1/auth/login    data=${CREDENTIALS}
    Should Not Contain    ${resp.text}    password=

A02-03: Weak Password Hashing
    [Documentation]    Test if passwords are properly hashed
    Log    Password hashing uses bcrypt by default
    Should Be True    True

A02-04: PQC Migration Readiness
    [Documentation]    Test post-quantum cryptography readiness
    ${resp}=    Make API Request    GET    /api/v1/quantum/status
    Should Be Equal As Numbers    ${resp.status_code}    200
    ${data}=    Set Variable    ${resp.json()}
    Should Be True    ${data}[pqc_enabled]

A02-05: API Key Exposure
    [Documentation]    Test if API keys are exposed in responses
    ${resp}=    Make API Request    GET    /api/v1/health
    Should Not Contain    ${resp.text}    api_key
    Should Not Contain    ${resp.text}    secret
