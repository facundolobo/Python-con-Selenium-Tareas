from selenium import webdriver

import time


driver = webdriver.Chrome("chromedriver.exe") #se agrego a la carpeta path de usuario y sistema" C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\"
driver.get("file:///C:/Users/ARMAGEDOM/Desktop/CURSO%20SELENIOM%20CON%20PYTHON/ejemplos%20python%20selenium/confirm_alert.html")
time.sleep(5)

confirm_alert = driver.find_element_by_name("confirm_alert")
confirm_alert.click()
time.sleep(3)

confirm_alert = driver.switch_to_alert()

confirm_alert.accept()
time.sleep(3)
driver.close()