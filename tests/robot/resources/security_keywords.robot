*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    OperatingSystem
Library    String

*** Variables ***
${BASE_URL}    http://localhost:8000
${API_BASE}    ${BASE_URL}/api/v1
${VALID_TOKEN}    test-jwt-token
${SAMPLE_IOC}    {"ioc_type": "ip_address", "value": "192.168.1.1", "source": "security-test"}
${VALID_CREDENTIALS}    {"username": "admin", "password": "secure-password"}
${EMPTY_HEADERS}    {"Content-Type": "application/json"}
${USER_HEADERS}    {"Content-Type": "application/json", "Authorization": "Bearer user-token"}
${ADMIN_HEADERS}    {"Content-Type": "application/json", "Authorization": "Bearer admin-token"}
${UNAUTHORIZED_HEADERS}    {"Content-Type": "application/json"}

*** Keywords ***
Make API Request
    [Arguments]    ${method}    ${endpoint}    ${data}=${None}    ${headers}=${None}
    ${default_headers}=    Create Dictionary    Content-Type    application/json
    Run Keyword If    ${headers} is not None    Set To Dictionary    ${default_headers}    &{headers}
    ${response}=    Run Keyword If    '${method}' == 'GET'    GET On Session    api    ${endpoint}    headers=${default_headers}    expected_status=any
    ...    ELSE IF    '${method}' == 'POST'    POST On Session    api    ${endpoint}    json=${data}    headers=${default_headers}    expected_status=any
    ...    ELSE IF    '${method}' == 'PUT'    PUT On Session    api    ${endpoint}    json=${data}    headers=${default_headers}    expected_status=any
    ...    ELSE IF    '${method}' == 'DELETE'    DELETE On Session    api    ${endpoint}    headers=${default_headers}    expected_status=any
    ...    ELSE IF    '${method}' == 'OPTIONS'    OPTIONS On Session    api    ${endpoint}    headers=${default_headers}    expected_status=any
    RETURN    ${response}

Get Header Value
    [Arguments]    ${response}    ${header_name}
    ${value}=    Get From Dictionary    ${response.headers}    ${header_name}    default_not_found
    RETURN    ${value}

Validate No Sensitive Data Exposed
    [Arguments]    ${response_text}
    Should Not Contain    ${response_text}    password
    Should Not Contain    ${response_text}    secret
    Should Not Contain    ${response_text}    api_key
    Should Not Contain    ${response_text}    private_key
    Should Not Contain    ${response_text}    stacktrace
    Should Not Contain    ${response_text}    traceback

Validate JSON Response
    [Arguments]    ${response}
    Should Be Equal As Numbers    ${resp.status_code}    200
    Should Contain    ${resp.headers}[Content-Type]    application/json
