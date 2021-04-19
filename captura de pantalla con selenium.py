from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.youtube.com/c/NicolasAlvarez_99/videos')
driver.get_screenshot_as_file("C:\\Users\\ARMAGEDOM\\Desktop\\CURSO SELENIOM CON PYTHON\\ejemplos python selenium\\mi canal de youtube.png")
driver.quit()
