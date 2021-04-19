import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para ingreso de texto por teclado
import time #para el tiempo de carga de pagina

class usando_unittest(unittest.TestCase):
    def setUp(self): #inicializar el driver
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

    def test_buscar_por_path(self): #recordar primero escribir test_
            driver = self.driver
            driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
            time.sleep(3)
            Toogle = driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/label[3]/div")
            
            Toogle.click() #realizar un click
            time.sleep(3)

            Toogle.click() #realizar un click
            time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
