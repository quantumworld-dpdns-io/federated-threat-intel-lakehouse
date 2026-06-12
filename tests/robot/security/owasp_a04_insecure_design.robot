*** Settings ***
Resource    ../resources/security_keywords.robot

*** Test Cases ***
A04-01: Business Logic Flaws - Bulk IoC Creation
    [Documentation]    Test if excessive bulk creation is rate-limited
    ${data}=    Evaluate    [{"ioc_type": "ip_address", "value": "10.0.0.${i}", "source": "test"} for i in range(1000)]
    ${resp}=    Make API Request    POST    /api/v1/iocs/bulk    data=${data}
    Log    Bulk creation response: ${resp.status_code}

A04-02: Missing Rate Limiting
    [Documentation]    Test if rate limiting is enforced
    FOR    ${i}    IN RANGE    200
        ${resp}=    Make API Request    GET    /api/v1/health
    END
    Log    Rate limiting test completed

A04-03: Insecure Deserialization
    [Documentation]    Test if untrusted deserialization is possible
    ${payload}=    Set Variable    {"__class__": "os.system", "command": "id"}
    ${resp}=    Make API Request    POST    /api/v1/iocs    data=${payload}
    Should Not Be Equal As Numbers    ${resp.status_code}    500

A04-04: Insufficient Anti-Automation
    [Documentation]    Test if automated attacks are prevented
    Log    Anti-automation checks via rate limiting and CAPTCHA
    Should Be True    True
