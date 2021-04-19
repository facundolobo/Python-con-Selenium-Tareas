from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.w3schools.com/tags/att_default.asp')
time.sleep(5)

all_cookies = driver.get_cookies() #obtener cookies

print(all_cookies)