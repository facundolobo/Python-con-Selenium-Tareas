from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\Users\ARMAGEDOM\Desktop\CURSO SELENIOM CON PYTHON\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/doodles")
driver.close() 