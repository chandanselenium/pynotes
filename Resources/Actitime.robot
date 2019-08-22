*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/PO/LandingPage.robot
Resource  ../Resources/PO/LoginPage.robot

*** Keywords ***
Navigate to app
  Enter the test url

Login to app
  Login

