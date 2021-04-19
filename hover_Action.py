from selenium import webdriver
from selenium.webdriver import ActionChains #para movimiento en el mouse
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com")

time.sleep(3)

elem= driver.find_element_by_link_text("Privacidad")

hover = ActionChains(driver).move_to_element(elem) #accion para mover al puntero al elem

hover.perform() 



