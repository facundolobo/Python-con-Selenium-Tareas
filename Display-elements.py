from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para uso del teclado
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com")

displayElement= driver.find_element_by_name("btnI")

print(displayElement.is_displayed()) #regresa true o false si ya cargo el elemento
print(displayElement.is_enabled()) #regresara un true o false si el elemento esta disponible
