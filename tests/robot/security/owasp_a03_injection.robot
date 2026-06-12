*** Settings ***
Resource    ../resources/security_keywords.robot

*** Test Cases ***
A03-01: SQL Injection - IoC Search
    [Documentation]    Test SQL injection via search endpoint
    ${payload}=    Set Variable    ' OR '1'='1' --
    ${resp}=    Make API Request    POST    /api/v1/iocs/search    data={"query": "${payload}"}
    Should Not Contain    ${resp.text}    syntax error
    Should Not Contain    ${resp.text}    sql

A03-02: NoSQL Injection
    [Documentation]    Test NoSQL injection via query parameters
    ${payload}=    Set Variable    {"$gt": ""}
    ${resp}=    Make API Request    GET    /api/v1/iocs?ioc_type=${payload}
    Should Not Be Equal As Numbers    ${resp.status_code}    500

A03-03: OS Command Injection
    [Documentation]    Test command injection via user input
    ${payload}=    Set Variable    ; cat /etc/passwd
    ${resp}=    Make API Request    POST    /api/v1/iocs    data={"value": "${payload}", "ioc_type": "ip_address", "source": "test"}
    Should Not Contain    ${resp.text}    root:

A03-04: Server-Side Template Injection
    [Documentation]    Test SSTI via input fields
    ${payload}=    Set Variable    {{7*7}}
    ${resp}=    Make API Request    POST    /api/v1/iocs    data={"description": "${payload}", "ioc_type": "ip_address", "value": "1.2.3.4", "source": "test"}
    Should Not Contain    ${resp.text}    49

A03-05: GraphQL Injection
    [Documentation]    Test GraphQL injection if GraphQL endpoint exists
    ${payload}=    Set Variable    {"query": "{ __schema { types { name } } }"}
    ${resp}=    Make API Request    POST    /graphql    data=${payload}
    Log    GraphQL endpoint test completed

A03-06: LDAP Injection
    [Documentation]    Test LDAP injection via authentication
    ${payload}=    Set Variable    admin)(&)
    ${resp}=    Make API Request    POST    /api/v1/auth/login    data={"username": "${payload}", "password": "test"}
    Should Not Be Equal As Numbers    ${resp.status_code}    200
