*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Open the browser
  Open Browser  about:blank  ${BROWSER}

Close the browser
  Close Browser

Setting the data base
  Log  setting the from data base

Ending the data base
  Log  ending the data from data base