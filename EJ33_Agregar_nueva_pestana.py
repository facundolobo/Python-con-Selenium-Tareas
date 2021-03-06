import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By #para tener acceso a la pagina
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def test_manejando_ventanas(self):
        self.driver.get("https://www.google.com/intl/es/gmail/about/#")
        time.sleep(4)
        self.driver.fullscreen_window()
        siguiente = self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/ul[1]/li/div/div/div[1]/div/div[3]/a[1]")
        siguiente.click()
        print(self.driver.current_window_handle)
        time.sleep(4)

        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle) #obtiene los datos de cada pestaña
            print(self.driver.title)
             


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    