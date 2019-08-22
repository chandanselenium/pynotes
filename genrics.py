from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging
import time
import math
class Elements:
    def __init__(self,driver):
        self.driver=driver
        self.ac=ActionChains(self.driver)

    def getElement(self, locator_type):
        element=locator_type.lower()
        if element=='id':
            return By.ID
        elif element=='name':
            return By.NAME
        elif element=='xpath':
            return By.XPATH
        else:
            print('locator of type ',locator_type,' is not found')



    def findElement(self, locator_type, locatore_value):
        try:
            element=locator_type.lower()
            getbytype=self.getElement(element)
            web_element=self.driver.find_element(getbytype,locatore_value)
            logging.info(('element with locator type ',locator_type,' and locator value ',locatore_value,' is found'))
        except:
            logging.info(('element not found with locator type ', locator_type, ' and locator value ', locatore_value,))
        return web_element

    def clickOnElement(self, locator_type, locator_value):
        try:
            element=locator_type.lower()
            web_element=self.findElement(element, locator_value)
            web_element.click()
            logging.info(('clicked on element with locator type ', locator_type, ' and locator value ', locator_value))
        except:
            logging.info(('cannot click on element with locator type ', locator_type, ' and locator value ', locator_value))




    def enterInputIn(self, locator_type, locator_value, data):
        try:
            element=locator_type.lower()
            web_element=self.findElement(element, locator_value)
            web_element.send_keys(data)
            logging.info(('entered input in element with locator type ', locator_type, ' and locator value ', locator_value))
        except:
            logging.info(('cannot enter the input in element with locator type ', locator_type, ' and locator value ', locator_value))


    def actionsChain(self,locator_type,locator_value,action):
        try:
            element=locator_type.lower()
            self.web_element=self.findElement(element,locator_value)

            if action=='rightclick':
                self.ac.context_click(self.web_element).perform()
            elif action=='doubleclick':
                self.ac.double_click(self.web_element).perform()
            elif action=='movetoelement':
                self.ac.move_to_element(self.web_element).perform()
            else:
                print(action,' action not found')
        except:
            logging.info(('cannot enter the input in element with locator type ', locator_type, ' and locator value'))


class Demo(Elements):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    def test(self):
        self.driver.get('https://www.flipkart.com')
        time.sleep(10)
        self.actionsChain('xpath','//span[text()="Men"]','movetoelement')


driver=webdriver.Chrome()
obj=Demo(driver)
obj.test()

math.factorial()