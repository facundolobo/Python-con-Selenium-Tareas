from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.amazon.com.mx/')
time.sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") #para ir al final de la pagina
time.sleep(3)
driver.close()
