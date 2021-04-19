from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

opciones = Options()

# enviar arguemntos (1 permitiendo la notificacion, 2 bloquean la notificacion)
opciones.add_experimental_option("prefs",{
    "profile.default_content_setting_value.notifications" : 2
})

driver = webdriver.Chrome(chrome_options=opciones, executable_path="chromedriver.exe")
driver.get('https://www.facebook.com/')
time.sleep(3)
