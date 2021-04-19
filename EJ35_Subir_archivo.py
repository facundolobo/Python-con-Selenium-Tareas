import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
    
    def test_subir_archivo(self):  
        self.driver.get("https://mdbootstrap.com/docs/standard/plugins/file-upload/")
        time.sleep(4)
        self.driver.find_element_by_id('input-file-now').send_keys('E:\imagen_subir.jpg')
        time.sleep(4)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
    