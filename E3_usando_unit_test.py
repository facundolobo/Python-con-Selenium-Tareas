import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para ingreso de texto por teclado
import time #para el tiempo de carga de pagina

class usando_unittest(unittest.TestCase):


	def setUp(self): #inicializar el driver
		self.driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

	
	def test_buscar(self): #recordar primero escribir test_
		driver= self.driver
		driver.get("http://www.google.com") #ingresamo a esa direccion

		self.assertIn("Google",driver.title) #vinculamos titulo
		
		elemento=driver.find_element_by_name("q") #asi se llama la varra de navegacion
		elemento.send_keys("selenium") #ingresamos al input
		elemento.send_keys(Keys.RETURN) #es lo mismo que enter"
		
		time.sleep(5)
		assert "no se encontro el elemento:" not in driver.page_source
	
	
	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()