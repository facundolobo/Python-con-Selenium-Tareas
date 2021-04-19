import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

import time


class usando_unittest(unittest.TestCase):
        def setUp(self): #inicializar el driver
            self.driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

        def test_usando_select(self):
            driver = self.driver
            driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
            time.sleep(3)
            
            select= driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select") 
            opcion = select.find_elements_by_tag_name("option") #guardara todas las opciones en esta variable
            time.sleep(3)
            
            for option in opcion:
                print("los valores son: %s " % option.get_attribute("value")) #mostramos los valores 
                option.click()
                time.sleep(1)
                
            seleccionar = Select(driver.find_element_by_xpath("//*[@id='main']/div[3]/div[1]/select")) # vinculamos al elemento 
            seleccionar.select_by_value("10") #solo seleccionar el elementos de la pocicion 10
            time.sleep(3)


if __name__ == '__main__':
    unittest.main()