'''
Robot Framework
'''
'''
supporting url:
1.==> https://robotframework.org
2.==> https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html

Overview:
Installation steps:
1. Install Python and pip(add to path)
2. use pip to install Robot Framework
3. use pip to install SeleniumLibrary
4. Select and install desired browser versions
5. Install selenium WebDriver for each browser
6. Install Pycharm and intellibot plugin
7. Create Base directory for script

################################################################################################################## 

1.Windows Cammand line and path Basis 
  1.1 command line:
     c:\     ==> to navigate to c drive
     c:> dir ==> to view all the files in 'c'
      
  1.1.1. create a file and open it through command line
            ex: e:>helloworld.txt
            ex: C:\Users\CHANDAN V>e:\helloworld.txt
            
  1.1.2. create a batch file by saving it by using .bat extension
            ex: helloworld.bat
                and 'echo' should be in the first word  
          execute the batch file by calling it in 'cmd'     
            ex: helloworld.bat     
                 
##################################################################################################################
2. Install Python and pip
    url ==> python.org
    2.1 In cmd type ==> python -V
    2.2 in cmd type ==> pip -V
    2.3 in cmd type ==> pip list 
    2.4 in cmd type ==> python -m pip install --upgrade pip   ==> to update pip 
    
##################################################################################################################    
3. Install Robot Framework and Selenium Library
     
      3.1 Install Robot Framework
           in cmd type ==> pip install robotframework
           
      3.2 Install selenium-Library
           in cmd type ==> pip install robotframework-seleniumlibrary

##################################################################################################################
4. Select the browser and download the required browser executables

##################################################################################################################
5. Install Pycharm and intellibot
        
        5.1 Install Pycharm
        5.2 install intellibot plugin
            1. navigate to settings
            2. click on plugin
            3. click on browse repository
            4. enter intellibot 
            5. install intellibot with selenium library (2nd option)

##################################################################################################################            
6. Create a new project 
    
    create 3 directory for the projects
    1==> Tests
    2==> Resources
    3==> Results          
        
###############################################################################################
7. Sections of the script file
   
   1.Settings
   2.Variables
   3.Test Cases
   4.Keywords(optional)

#############################################################################################   
8. Executing the program.
    To execute the program we use terminal
    In terminal we should enter the below command
       ==> robot -d Results Tests/Actitime.robot
       
##################################################################################################################

Level 1:create a more readable script

1.1 user defined keywords
      
*** Settings ***

*** Test Cases ***

test case 1

  Do Something
  Do Something else

test case 2

  Do Another Thing
  Do Another Thing Else

*** Keywords ***

Do Something
  log  i am doing something

Do Another Thing
  log  i am doing another thing

Do Another Thing Else
  log  i am doing another thing else

Do Something Else
  log  i am doing something else       

##################################################################################################################
1.2 Break up scripts into keywords

 set up 1 ==> give comments in the required places
 set up 2 ==> add the comment implimation in the keyword section
 
##################################################################################################################
1.3 Moving keywords to the resources file
   
   1. create a file in 'resource' with name as actitime.robot
   2. create a file in 'resource' with name as commom.robot
   3. in resource/amazon.robot past all the keywords from the script and import this module in 
      the test case file
   4. in the resource/common.robot past the launch the browser and close the browser command
       and import in the test case file
       
       program in resource/actitime
       *** Settings ***
        Library  SeleniumLibrary
        
        *** Keywords ***
        Open the browser enter test url
          Open Browser  about:blank  chrome
        
        Enter the test url
          Go TO  https://online.actitime.com/testyantra3/login.do
          sleep  3s
        
        Login
          Input Text  id=username  admin
          Input Text  name=pwd  manager
          Click Link  id=loginButton
          sleep  5s
               
       
       
       program in resource/common
       *** Settings ***
        Library  SeleniumLibrary
        
        *** Keywords ***
        Open the browser
          Open Browser  about:blank  chrome
        
        Close the browser
          Close Browser
       
       
       
       
       
###############################################################################################
1.4 Adding setup and teardown       

program in test/actitime
    *** Settings ***
        Documentation  This is the Login script for Actitme
        Resource  ../Resources/Actitime.robot
        Resource  ../Resources/Common.robot
        Suite Setup  Setting the data base
        Test Setup  Open the browser
        Test Teardown  Close the browser
        Suite Teardown  Ending the data base     
        
        *** Variables ***
        
        
        *** Test Cases ***
        test 1
          [Documentation]  This is login script for Actitime
          [Tags]  Smoke
        
          Enter the test url
          Login       
        
        test 2
          Enter the test url
          Login
      
program in common
        *** Settings ***
        Library  SeleniumLibrary
        
        *** Keywords ***
        Open the browser
          Open Browser  about:blank  chrome
        
        Close the browser
          Close Browser 
        
        Setting the data base
          Log  setting the from data base
        
        Ending the data base
          Log  ending the data from data base
    
###############################################################################################
1.5 POM Page object module

  1. create files PO==> page object in resources file
  2. create LandingPage.robot in PO
  3. create LoginPage.robot in po
  
program in LandingPage.robot
         
        *** Settings ***
        Library  SeleniumLibrary
        
        *** Keywords ***        
        Enter the test url
          Go TO  https://online.actitime.com/testyantra3/login.do
          sleep  3s     
          
program in LoginPage.robot
        *** Settings ***
        Library  SeleniumLibrary
        
        *** Keywords ***
        Login
          Input Text  id=username  admin
          Input Text  name=pwd  manager
          Click Link  id=loginButton
          sleep  5s  
          
program in Resources/Actitime.robot
        *** Settings ***
        Library  SeleniumLibrary
        Resource  ../Resources/PO/LandingPage.robot
        Resource  ../Resources/PO/LoginPage.robot
        
        *** Keywords ***
        Navigate to app
          Enter the test url
        
        Login to app
          Login      
          
program in Tests/Actitime.robot

        *** Settings ***
        Documentation  This is the Login script for Actitme
        Resource  ../Resources/Actitime.robot
        Resource  ../Resources/Common.robot
        Suite Setup  Setting the data base
        Test Setup  Open the browser
        Test Teardown  Close the browser
        Suite Teardown  Ending the data base        
        
        *** Variables ***        
        
        *** Test Cases ***
        test 1
          [Documentation]  This is login script for Actitime
          [Tags]  Smoke
        
          Enter the test url
          Login to app        
        
        test 2
          Enter the test url
          Login to app   

###############################################################################################                             
1.6 adding variables to the script

        *** Settings ***
        Documentation  This is the Login script for Actitme
        Resource  ../Resources/Actitime.robot
        Resource  ../Resources/Common.robot
        Suite Setup  Setting the data base
        Test Setup  Open the browser
        Test Teardown  Close the browser
        Suite Teardown  Ending the data base
        
        
        *** Variables ***
        ${TESTURL}=  https://online.actitime.com/testyantra3/login.do
        ${BROWSER}=  chrome
        ${USERNAME}=  admi
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
 
###############################################################################################    
1.7 Passing input from cmd
      robot -d results -v BROWSER:FIREFOX tests/actitime.robot
 
###############################################################################################      
1.8 Using variable in Pom
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
          
###############################################################################################
1.9 Add quotes for keywords for clarity
             
###############################################################################################

2. Agenda
    
    Explore the Library
        1. BuiltIn
        2. Dialogs
        3. Operating System
        4. DataBase
        5. API
        6. XML
        7. String
        8. Selenium2
        
1. BuiltIN
  
  nothing to install
  Log/Comments
  convertions
  "run Keyword(s)" options
  Repeat Keyword
  Set variables(test,suit, global)
  should(contains|be equal)/should Not
  sleep
  wait until Keyword Succeeds(!)
   
###############################################################################################
        
        
web locators


                      
'''
