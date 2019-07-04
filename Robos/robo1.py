from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso Robô ... \n")

driver = webdriver.Chrome(r"C:\Users\a0044443\PycharmProjects\RPA-Python2\venv\chromedriver.exe")
driver.get("https://registro.br/")

pesquisa = driver.find_element_by_id("is-avail-field")
pesquisa.clear()#limpa pesquisa
dominio = "udemy.com.br"
pesquisa.send_keys(dominio)
pesquisa.send_keys(Keys.RETURN)
time.sleep(2)

resultados = driver.find_elements_by_tag_name("strong")
#import pdb; pdb.set_trace() #parando a execução para fazer trace
print("Domínio %s %s" % (dominio, resultados[4].text))


time.sleep(6)
driver.close()

