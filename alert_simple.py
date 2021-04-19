from selenium import webdriver

import time


driver = webdriver.Chrome("chromedriver.exe") #se agrego a la carpeta path de usuario y sistema" C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\"
driver.get("file:///C:/Users/ARMAGEDOM/Desktop/CURSO%20SELENIOM%20CON%20PYTHON/ejemplos%20python%20selenium/alert_simple.html")

alerta_simple = driver.find_element_by_name("alert")

alerta_simple.click()

time.sleep(3)

alerta_simple = driver.switch_to_alert() #cambia a una ventana 

alerta_simple.dismiss() #click al unico boton que tiene
time.sleep(3)
driver.close() 