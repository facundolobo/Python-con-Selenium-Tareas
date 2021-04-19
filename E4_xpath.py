import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para ingreso de texto por teclado
import time #para el tiempo de carga de pagina

class usando_unittest(unittest.TestCase):

    def setUp(self): #inicializar el driver
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

    def test_buscar_por_path(self): #recordar primero escribir test_
            driver = self.driver
            driver.get("http://www.google.com")
            buscar_por_xpath= driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
            time.sleep(3)
            buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN) #escribir selenium y apretar flecha para abajo
            time.sleep(6)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
