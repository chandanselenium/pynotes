*** Settings ***
Library  SeleniumLibrary

*** Keywords ***

Enter the test url
  Go TO  ${TESTURL}
  sleep  3s