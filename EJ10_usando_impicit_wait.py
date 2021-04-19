import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC #poara establecer una condicion para continuar la automatizacion

#import time #para el tiempo de carga de pagina

class usando_unittest(unittest.TestCase):
    def setUp(self): #inicializar el driver
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

    def test_usando_impicit_wait(self): #recordar primero escribir test_
        driver = self.driver
        driver.implicitly_wait(5) #espera como maximo 5 segundo funcion de selenium , el timer es de python
        driver.get("https://www.google.com")
        myDynamicElement = driver.find_elements_by_name("q")


        
        

if __name__ == '__main__':
    unittest.main()