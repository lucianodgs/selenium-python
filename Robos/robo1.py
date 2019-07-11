#Author: Luciano Diniz
#Exercico do "curos Criando Robôs em Python - Automatizando Processos"
#URL: https://www.udemy.com/criando-robos-em-python/
#
#  Esse exercico irá ler uma lista de dominios no site https://registro.br/ e verificar
#se o dominio já está registrado dando um print com o status do dominio.
# Este código está com algumas chamadas a time.sleep para qu o resultado em tela seja melhor observado.
##
##---- Python ----
#https://www.python.org/downloads/release/python-360/

##---- Bibliotecas ----
#xlrd, selenium, requests

##---- Driver Selenium ----
#http://chromedriver.chromium.org/downloads

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando nosso Robô ... \n")

#Leitura do arquivo do excel
workbook = xlrd.open_workbook(r"dominio.xlsx",ragged_rows=True)

#Copia a primeira planilha do arquivo EXCEL para uma variável tipo Sheet
sheet = workbook.sheet_by_index(0)
dominios = []

# Transforma a primeira coluna da planilha em uma lista
#Neste ponto há uma alteração em relação ao exemplo do curso. Eu adicionei a funnção sheet.cell_value e a varievel sheet.nrows para saber o numero de linhas preenchidas da planilha
for linha in range(sheet.nrows):
    dominios.append(sheet.cell_value(linha,0))

#import pdb; pdb.set_trace() #parando a execução para fazer trace

#Chama a biblioteca do selenium para abrir o google Chome
driver = webdriver.Chrome(r"..\chromedriver.exe")
driver.get("https://registro.br/")

#busca na página a informação desejada
for dominio in dominios:
    #Aqui localizamos o objeto em tela pelo ID. Para saber o ID precisamos inspecionar o código html da pagina https://registro.br/  e localizar o ID
    #O google chrome tem a opção inspect que ajuda nese  trabalho
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear()  # limpa pesquisa
    pesquisa.send_keys(dominio) #preenche o campo localizado
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)
    resultados = driver.find_elements_by_tag_name("strong")
    print("Domínio %s %s" % (dominio, resultados[4].text))

time.sleep(6)
driver.close()

