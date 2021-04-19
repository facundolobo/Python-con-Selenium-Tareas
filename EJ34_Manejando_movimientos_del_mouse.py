import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains #funciones click mouse
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
    
    def test_manejando_mouse(self):
        self.driver.get("https://www.w3schools.com/css/css_dropdowns.asp")
        time.sleep(4)
        mouse_nov = self.driver.find_element_by_xpath("//*[@id='main']/div[3]/div[2]/div/button") 
        mouse_nov2 = self.driver.find_element_by_xpath("//*[@id='main']/div[3]/div[2]/div/div/a[1]")
        movimiento = ActionChains(self.driver)
        movimiento.move_to_element(mouse_nov).move_to_element(mouse_nov2).click().perform() #mueve el mouse al meno desplegable y luego a la primera opcion y luego click
        time.sleep(3)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    