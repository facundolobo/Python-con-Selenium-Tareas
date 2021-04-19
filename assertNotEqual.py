import unittest
from selenium import webdriver
import time
class suite(unittest.TestCase):
    def setUp(self):
        self.cdrive = webdriver.Chrome("chromedriver.exe")
    
    #tantos test como quiera pero debe tener prefijo test_
    def test_assertNotEqual(self):
        
        cdrive= self.cdrive
        cdrive.get("http://www.google.com")
        tituloDeLaPagina= cdrive.title
        self.assertNotEqual("Google1" , tituloDeLaPagina , "El titulo de la pagina no es igual")
    
    
       
    # para limpieza de variables
    def tearDown(self):
        self.cdrive.quit()


if __name__ == '__main__':
    unittest.main()
