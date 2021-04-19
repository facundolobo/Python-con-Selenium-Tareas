import configparser #parcear una configuracion para guardarla en un archivo 

configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome' : 'E:\chromedriver_win32\chromedriver.exe'}
configuracion['Paginas'] = {'page' : 'http://www.google.com.mx'}

with open('configuracion.ini' , 'w') as archivoconfig:
    configuracion.write(archivoconfig)