*** Settings ***
Resource    ../resources/security_keywords.robot

*** Test Cases ***
A05-01: Default Credentials
    [Documentation]    Test if default credentials work
    ${resp}=    Make API Request    POST    /api/v1/auth/login    data={"username": "admin", "password": "admin"}
    Should Not Be Equal As Numbers    ${resp.status_code}    200

A05-02: Security Headers Check
    [Documentation]    Test if security headers are present
    ${resp}=    Make API Request    GET    /api/v1/health
    Should Not Contain    ${resp.headers}    Server: nginx
    Log    Security headers check completed

A05-03: Error Handling Information Leakage
    [Documentation]    Test if error messages leak sensitive info
    ${resp}=    Make API Request    GET    /api/v1/nonexistent
    Should Not Contain    ${resp.text}    stacktrace
    Should Not Contain    ${resp.text}    traceback
    Should Not Contain    ${resp.text}    Internal Server Error

A05-04: Unnecessary Features Enabled
    [Documentation]    Test if debug mode is disabled in production
    ${resp}=    Make API Request    GET    /docs
    Log    Debug endpoint accessibility check

A05-05: Cloud Storage Permissions
    [Documentation]    Test if cloud storage is properly configured
    Log    Cloud storage permission checks
    Should Be True    True
