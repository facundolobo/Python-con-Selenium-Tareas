from selenium import webdriver

from selenium.webdriver.common.keys import Keys #para ingreso de texto por teclado

import time #para el tiempo de carga de pagina


#driver = webdriver.Firefox(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\geckodriver-v0.29.0-win64\geckodriver.exe") #para usar el drive que descargamos para ontrolar chrome

driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

driver.get("https://gmail.com") #ir a esta pagina

usuario = driver.find_element_by_id("identifierId") #vincular con el campo correo
usuario.send_keys("facundolobo2@gmail.com")  #ingresamos correo

usuario.send_keys(Keys.ENTER) #presionamos enter
time.sleep(3)


clave = driver.find_element_by_name("password")#vincular con el campo clave
calve.send_keys("123213")
calve.send_keys(Keys.ENTER) #presionamos enter




