from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import xlrd

options = webdriver.ChromeOptions()

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

arq = open("resultado.txt", "w")
workbook = xlrd.open_workbook(r'C:\Users\mthen\OneDrive\Documentos\my_codes\first_robot\bots_python\arquivos\excel\arquivo.xls')
sheet = workbook.sheet_by_name('Plan1')
rows = sheet.nrows
columns = sheet.ncols

driver.get('https://registro.br/')
time.sleep(1)

for curr_row in range(0, rows):
    time.sleep(1)
    x = sheet.cell_value(curr_row, 0)
    pesquisa = driver.find_element(By.ID,"is-avail-field")
    time.sleep(1)
    pesquisa.clear()
    time.sleep(1)
    pesquisa.send_keys(x)
    time.sleep(1)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong')
    
    texto = "Dominio %s %s\n" % (x, driver.find_element(By.XPATH, '//*[@id="app"]/main/section/div[2]/div/p/span/strong').text)
    arq.write(texto)
    

arq.close()
driver.quit()