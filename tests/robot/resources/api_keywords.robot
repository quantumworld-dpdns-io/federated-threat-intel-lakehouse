*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Keywords ***
Create IoC
    [Arguments]    ${ioc_type}    ${value}    ${source}=test    ${severity}=medium
    ${data}=    Create Dictionary    ioc_type=${ioc_type}    value=${value}    source=${source}    severity=${severity}
    ${resp}=    POST On Session    api    /api/v1/iocs    json=${data}    expected_status=201
    RETURN    ${resp.json()}

Get IoC
    [Arguments]    ${ioc_id}
    ${resp}=    GET On Session    api    /api/v1/iocs/${ioc_id}    expected_status=200
    RETURN    ${resp.json()}

List IoCs
    [Arguments]    ${page}=1    ${page_size}=20
    ${resp}=    GET On Session    api    /api/v1/iocs?page=${page}&page_size=${page_size}    expected_status=200
    RETURN    ${resp.json()}

Search IoCs
    [Arguments]    ${query}
    ${data}=    Create Dictionary    query=${query}
    ${resp}=    POST On Session    api    /api/v1/iocs/search    json=${data}    expected_status=200
    RETURN    ${resp.json()}

Create Campaign
    [Arguments]    ${name}    ${description}    ${severity}=medium
    ${data}=    Create Dictionary    name=${name}    description=${description}    severity=${severity}
    ${resp}=    POST On Session    api    /api/v1/campaigns    json=${data}    expected_status=201
    RETURN    ${resp.json()}

Check Health
    ${resp}=    GET On Session    api    /api/v1/health    expected_status=200
    RETURN    ${resp.json()}
