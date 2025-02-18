#pyinstaller --onefile script.py

import time #adicionar pausas no codigo
from selenium import webdriver #webdriver controla o navegador
from selenium.webdriver.common.by import By #classe By, usada para localizar elementos na página (como a barra de pesquisa)
from selenium.webdriver.common.keys import Keys #Keys, que permite simular o pressionamento de teclas, como Enter

options = webdriver.EdgeOptions() #Cria opções de configuração para o navegador
driver = webdriver.Edge(options=options) #Abre o navegador Edge com as configurações definidas

try:
    
    driver.get("https://www.google.com") #Faz o navegador acessar o site especificado (neste caso, o Google). 

    search_box = driver.find_element(By.NAME, "q") #find_element(By.NAME, "q") → Localiza o campo de pesquisa do Google e q é o nome do elemento da barra de pesquisa no Google

    search_box.send_keys("Selenium WebDriver")
    search_box.send_keys(Keys.RETURN)

    time.sleep(15)

    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Automação com Python")
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)

finally:
    driver.quit()
