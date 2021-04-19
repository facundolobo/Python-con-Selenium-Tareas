from selenium import webdriver
from selenium.webdriver import ActionChains #para movimiento en el mouse
import time

palabra_busqueda = "sele"

driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com")

time.sleep(5)

busqueda = driver.find_element_by_name("q")
busqueda.send_keys(palabra_busqueda)
time.sleep(5)

for i in range(1,11):
    elementos = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/ul/li["+str(i)+"]/div/div[2]/div[1]/span").text
    print(palabra_busqueda + elementos)

driver.close()