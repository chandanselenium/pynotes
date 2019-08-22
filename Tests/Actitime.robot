*** Settings ***
Documentation  This is the Login script for Actitme
Resource  ../Resources/Actitime.robot
Resource  ../Resources/Common.robot
Suite Setup  Setting the data base
Test Setup  Open the browser
Test Teardown  Close the browser
Suite Teardown  Ending the data base


*** Variables ***
${TESTURL}=      https://online.actitime.com/testyantra3/login.do
${BROWSER}=  chrome
${USERNAME}=  admin
${PASSWORD}=  manager


*** Test Cases ***
test 1
  [Documentation]  This is login script for Actitime
  [Tags]  Smoke

  Enter the test url
  Login to app


test 2
  Enter the test url
  Login to app

hai

