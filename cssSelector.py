from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para uso del teclado
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/html")
time.sleep(5)

content= driver.find_element_by_css_selector('a.w3-blue') #VINCULACION con ese campo link
content.click()
time.sleep(5)