*** Settings ***
Resource    ../resources/security_keywords.robot
Suite Teardown    Cleanup Security Test Suite

*** Test Cases ***
A01-01: Horizontal Privilege Escalation
    [Documentation]    Test if user A can access user B's resources
    ${resp}=    Make API Request    GET    /api/v1/iocs    headers=${UNAUTHORIZED_HEADERS}
    Should Be Equal As Numbers    ${resp.status_code}    401

A01-02: Vertical Privilege Escalation
    [Documentation]    Test if regular user can access admin endpoints
    ${resp}=    Make API Request    GET    /api/v1/admin/users    headers=${USER_HEADERS}
    Should Not Be Equal As Numbers    ${resp.status_code}    200

A01-03: IDOR - Insecure Direct Object Reference
    [Documentation]    Test if predictable IDs expose other users' data
    ${resp}=    Make API Request    GET    /api/v1/iocs/00000000-0000-0000-0000-000000000001    headers=${USER_HEADERS}
    Status Should Not Be    200    ${resp}

A01-04: CORS Misconfiguration
    [Documentation]    Test if CORS allows unauthorized origins
    ${headers}=    Create Dictionary    Origin    https://evil.com
    ${resp}=    Make API Request    OPTIONS    /api/v1/iocs    headers=${headers}
    ${acao}=    Get Header Value    ${resp}    Access-Control-Allow-Origin
    Should Not Be Equal    ${acao}    *    msg=CORS wildcard allowed for evil origin

A01-05: Directory Traversal
    [Documentation]    Test if path traversal is possible
    ${resp}=    Make API Request    GET    /api/v1/../../../etc/passwd    headers=${USER_HEADERS}
    Should Not Be Equal As Numbers    ${resp.status_code}    200

A01-06: Forced Browsing
    [Documentation]    Test if unauthenticated access to protected pages works
    ${resp}=    Make API Request    GET    /api/v1/federation/nodes    headers=${EMPTY_HEADERS}
    Should Not Be Equal As Numbers    ${resp.status_code}    200
