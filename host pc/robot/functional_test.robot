*** Settings ***
Documentation                       FT System Initial Test

Library                             FTLibrary

*** Test Cases ***
HUB Connected
    [Tags]    USB VCP Receive	USB Connection
    Wait Until Keyword Succeeds    3 sec    1 msec
    ...    Try To hub is connected
    [Teardown]    Run Keyword if Test Failed    Fatal Error

Digital IO connected
    [Tags]    USB VCP Receive	USB Connection
    Wait Until Keyword Succeeds    3 sec    1 msec
    ...    Try To digital io is connected

Analog IO connected
    [Tags]    USB VCP Receive	USB Connection
    Wait Until Keyword Succeeds    3 sec    1 msec
    ...    Try To analog io is connected

Read analog and digital IOs
    [Tags]    USB VCP Receive
    Wait Until Keyword Succeeds    3 sec    1 msec
    ...    Try To data is ok

Common timer enabled
    [Tags]    USB VCP Receive	USB VCP Transmit	Common timer
    Wait Until Keyword Succeeds    3 sec    1 msec
    ...    Try To enable timer
	
*** Variables ***