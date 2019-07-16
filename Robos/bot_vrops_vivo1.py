from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("Iniciando nosso Robô ... \n")

driver = webdriver.Chrome(r"C:\Users\a0044443\PycharmProjects\RPA-Python2\venv\chromedriver.exe")

usuario = "a0044443"
pass_pwd = ""



driver.get("https://10.238.5.28/ui/login.action")
driver.fullscreen_window()

box_dominio =  driver.find_element_by_id("authSelector-inputEl")
box_dominio.click()
box_dominio.send_keys(Keys.ARROW_DOWN)
box_dominio.send_keys(Keys.ARROW_DOWN)
box_dominio.send_keys(Keys.ENTER)

box_user_name = driver.find_element_by_id("userName-inputEl")
box_user_name.clear()#limpa pesquisa
box_user_name.send_keys(usuario)

box_pwd = driver.find_element_by_id("password-inputEl")
box_pwd.clear()#limpa pesquisa
box_pwd.send_keys(pass_pwd)
box_pwd.send_keys(Keys.ENTER)
time.sleep(6)
print("Login realizado...")

driver.get("https://10.238.5.28/ui/index.action#/environment/overview/applications")

bot1 = driver.find_element_by_id("ext-element-1")
bot1.click()
#bot1 = driver.find_element_by_id("button-1190-btnIconEl")
#environment = driver.find_element_by_xpath("//*[@id='tab-1249-btnInnerEl']")
#bot1.click()

time.sleep(5)
#import pdb; pdb.set_trace() #parando a execução para fazer trace

#application = driver.find_element_by_id("ext-element-16")
#application.send_keys(Keys.RETURN)

#time.sleep(2)
#box_pwd.send_keys(Keys.ENTER)


#resultados = driver.find_elements_by_tag_name("strong")
#import pdb; pdb.set_trace() #parando a execução para fazer trace
#print("Domínio %s %s" % (dominio, resultados[4].text))

driver.close()





