import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
    
    def test_subir_archivo(self):  
        self.driver.get("https://www.w3schools.com/jsref/event_oncontextmenu.asp") 
        time.sleep(4)
        clickDerecho = self.driver.find_element_by_xpath("//*[@id='main']/p[1]/a[2]")
        actions = ActionChains(self.driver)
        actions.context_click(clickDerecho).perform() #click derecho
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    