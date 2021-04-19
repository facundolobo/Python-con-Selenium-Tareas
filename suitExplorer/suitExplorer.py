import HtmlTestRunner
import unittest
from selenium import webdriver
import time
class suite(unittest.TestCase):
    def setUp(self):
        self.cdrive = webdriver.Chrome("chromedriver.exe")
    
    #tantos test como quiera pero debe tener prefijo test_
    def test_busqueda(self):
        self.cdrive.get("http://www.google.com")
        self.busqueda = self.cdrive.find_element_by_name("q")
        self.busqueda.send_keys("selenium")
        self.busqueda.submit() 
        time.sleep(3)
    
    def test_scroll_down(self):
        driver = self.cdrive
        driver.get('https://www.amazon.com.mx/')
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") #para ir al final de la pagina
        time.sleep(3)
       
    # para limpieza de variables
    def tearDown(self):
        self.cdrive.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='resultados de mi test plan'))

    
    