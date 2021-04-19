import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para ingreso de texto por teclado
import time #para el tiempo de carga de pagina

class usando_unittest(unittest.TestCase):
    def setUp(self): #inicializar el driver
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

    def test_pagina_anterior_o_siguiente(self): #recordar primero escribir test_
        driver = self.driver
        driver.get("https://www.google.com")
        time.sleep(3)
        driver.get("https://www.facebook.com")
        time.sleep(3)
        driver.get("https://www.ibm.com")
        time.sleep(3)
        driver.back() #regresar la pagina
        time.sleep(3)
        driver.back() #regresar la pagina
        time.sleep(3)
        driver.forward() #pagina siguiente 
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
