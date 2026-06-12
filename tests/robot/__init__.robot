*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    OperatingSystem
Library    String

Suite Setup    Initialize Test Environment
Suite Teardown    Cleanup Test Environment

*** Variables ***
${BASE_URL}    http://localhost:8000
${API_BASE}    ${BASE_URL}/api/v1
${VALID_TOKEN}    test-jwt-token

*** Keywords ***
Initialize Test Environment
    Log    Starting security test environment
    Create Session    api    ${BASE_URL}

Cleanup Test Environment
    Log    Cleaning up test environment
    Delete All Sessions

Make API Request
    [Arguments]    ${method}    ${endpoint}    ${data}=${None}    ${headers}=${None}
    ${default_headers}=    Create Dictionary    Content-Type    application/json
    Run Keyword If    ${headers} is not None    Set To Dictionary    ${default_headers}    &{headers}
    ${response}=    Run Keyword If    '${method}' == 'GET'    GET On Session    api    ${endpoint}    headers=${default_headers}
    ...    ELSE IF    '${method}' == 'POST'    POST On Session    api    ${endpoint}    json=${data}    headers=${default_headers}
    ...    ELSE IF    '${method}' == 'PUT'    PUT On Session    api    ${endpoint}    json=${data}    headers=${default_headers}
    ...    ELSE IF    '${method}' == 'DELETE'    DELETE On Session    api    ${endpoint}    headers=${default_headers}
    RETURN    ${response}
