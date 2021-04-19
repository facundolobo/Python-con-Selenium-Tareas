import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para ingreso de texto por teclado
import time #para el tiempo de carga de pagina

class usando_unittest(unittest.TestCase):
    def setUp(self): #inicializar el driver
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

    def test_cambiar_ventana(self): #recordar primero escribir test_
            driver = self.driver
            driver.get("https://www.google.com")
            time.sleep(3)
            driver.execute_script("window.open('');") #abrir otra ventana
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[1]) #posicionarte en la segunda ventana
            time.sleep(3)
            driver.get("https://www.facebook.com") #escribir esto en la otra ventana
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[0]) #posicionarte en la segunda ventana
            time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
