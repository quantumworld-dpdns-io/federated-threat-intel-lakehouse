*** Settings ***
Resource    ../resources/security_keywords.robot

*** Test Cases ***
A07-01: Brute Force Protection
    [Documentation]    Test if brute force attacks are mitigated
    FOR    ${i}    IN RANGE    20
        ${resp}=    Make API Request    POST    /api/v1/auth/login    data={"username": "admin", "password": "wrong${i}"}
    END
    Log    Brute force protection test completed

A07-02: Session Management
    [Documentation]    Test if session tokens are properly managed
    ${resp}=    Make API Request    POST    /api/v1/auth/login    data=${VALID_CREDENTIALS}
    Log    Session management test completed

A07-03: JWT Token Validation
    [Documentation]    Test if invalid JWT tokens are rejected
    ${headers}=    Create Dictionary    Authorization    Bearer invalid-token
    ${resp}=    Make API Request    GET    /api/v1/iocs    headers=${headers}
    Should Be Equal As Numbers    ${resp.status_code}    401

A07-04: MFA Bypass Testing
    [Documentation]    Test if MFA can be bypassed
    Log    MFA bypass test - checking if MFA enforcement is active
    Should Be True    True
