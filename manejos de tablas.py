from selenium import webdriver

import time


driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/html/html_tables.asp")

time.sleep(5)

valor = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr[2]/td[2]").text #toma todas los registros

print(valor)

rows = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr"))
col = len(driver.find_elements_by_xpath("//*[@id='customers']/tbody/tr[1]/th"))

print(rows) #obtener la cantidad de registros
print(col) #obtener la cantidad de col

for i in range(2, rows +1):
    for j in range( 1, col +1 ):
        dato = driver.find_element_by_xpath("//*[@id='customers']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        print(dato, end = '                         ')
    print()