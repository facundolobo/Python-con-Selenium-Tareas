from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para uso del teclado
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/")
time.sleep(5)

encontrar_link= driver.find_element_by_link_text("Learn PHP") #VINCULACION con ese campo link
encontrar_link.click()
time.sleep(5)