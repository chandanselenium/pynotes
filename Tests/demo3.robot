*** Settings ***
Library  seleniumlibrary


*** Test Cases ***
test 1
  open browser  https://google.com  chrome
  sleep  5s
  close