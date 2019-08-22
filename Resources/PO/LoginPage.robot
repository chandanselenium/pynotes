*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${USERNAME_TEXT_FIELD}=  id=username
${PASSWORD_TEXT_FIELD}=  name=pwd
${LOGIN_BUTTON}=  id=loginButton

*** Keywords ***
Login
  Input Text  ${USERNAME_TEXT_FIELD}  ${USERNAME}
  Input Text  ${PASSWORD_TEXT_FIELD}  ${PASSWORD}
  Click Link  ${LOGIN_BUTTON}
  sleep  5s