#pyinstaller --onefile script.py

import time #adicionar pausas no codigo]
import random #fazer escolhas aleatorias
from selenium import webdriver #webdriver controla o navegador
from selenium.webdriver.common.by import By #classe By, usada para localizar elementos na página (como a barra de pesquisa)
from selenium.webdriver.common.keys import Keys #Keys, que permite simular o pressionamento de teclas, como Enter

# Lista de termos de pesquisa aleatórios (150 tópicos variados)
search_terms = [
    "Receitas fáceis para o jantar", "Melhores destinos turísticos", "História do Egito Antigo", "Como cuidar de plantas em casa", 
    "Filmes mais assistidos de 2024", "Dicas para economizar dinheiro", "Curiosidades sobre o espaço", "Benefícios do chá verde",
    "Melhores exercícios para perder peso", "Como melhorar a memória", "Como fazer pão caseiro", "História da Segunda Guerra Mundial",
    "Animais mais perigosos do mundo", "Como meditar corretamente", "Diferença entre café e chá", "Dicas para uma boa noite de sono",
    "Alimentos ricos em proteínas", "O que fazer em um dia chuvoso", "Curiosidades sobre o oceano", "História da Torre Eiffel",
    "Lugares assombrados ao redor do mundo", "Como aprender um novo idioma", "Benefícios da caminhada diária", "Como fazer jardinagem em casa",
    "Por que os gatos ronronam?", "Os melhores livros de romance", "Como melhorar a produtividade", "Dicas para uma alimentação saudável",
    "Curiosidades sobre o corpo humano", "Os maiores mistérios do mundo", "Como organizar um casamento", "Como funciona a energia solar",
    "Dicas para viajar barato", "Os melhores parques nacionais", "Por que o céu é azul?", "Como treinar para uma maratona",
    "Como fazer um piquenique perfeito", "As cidades mais antigas do mundo", "Como preparar um café perfeito", "Dicas para fotografias incríveis",
    "Melhores raças de cães para apartamento", "Curiosidades sobre o cinema", "O que é a dieta mediterrânea?", "Os benefícios do yoga",
    "Como montar um aquário", "História da arte renascentista", "Como fazer um bolo de chocolate perfeito", "Diferença entre sonho e pesadelo",
    "Os efeitos do estresse no corpo", "Dicas para manter a casa organizada", "Como criar um orçamento pessoal", "Os segredos dos castelos medievais",
    "As civilizações antigas mais impressionantes", "Como fazer um smoothie saudável", "Os planetas mais intrigantes do sistema solar",
    "A importância da reciclagem", "Os mitos mais famosos da mitologia grega", "Como evitar o desperdício de alimentos",
    "Dicas para um cabelo mais saudável", "Os festivais culturais mais incríveis do mundo", "Como treinar um cachorro corretamente",
    "As melhores trilhas para caminhadas", "Como fazer um chá perfeito", "A história dos Jogos Olímpicos", "Os esportes mais populares do mundo",
    "Como preparar um jantar romântico", "Dicas para decorar pequenos espaços", "Os desertos mais bonitos do planeta",
    "Curiosidades sobre os vulcões", "Como funciona o cérebro humano", "Os maiores enigmas da arqueologia", "Os melhores destinos para lua de mel",
    "Como fazer artesanato com materiais recicláveis", "As pontes mais impressionantes do mundo", "O que são as auroras boreais?",
    "Como fazer uma horta em casa", "Os melhores documentários para assistir", "Dicas para um café da manhã saudável",
    "Os rios mais longos do mundo", "Como funciona a economia global", "Os segredos dos castelos encantados", "Dicas para um piquenique romântico",
    "Como cuidar de um gato filhote", "Os carros mais rápidos do mundo", "Curiosidades sobre a cultura japonesa",
    "Como fazer um bom churrasco", "Dicas para fotografar estrelas", "A história dos vikings", "Os mistérios do Triângulo das Bermudas",
    "O que fazer em Paris?", "Como aprender a tocar violão?", "A história do Coliseu de Roma", "Melhores praias do Brasil",
    "Como fazer uma mochila para trilhas?", "As florestas mais bonitas do mundo", "O que é o Efeito Mandela?",
    "Como cuidar de um peixe Betta", "Os melhores filmes de suspense", "Dicas para organizar uma festa surpresa",
    "Os cachorros mais inteligentes do mundo", "Como cozinhar sem óleo?", "Curiosidades sobre o deserto do Saara",
    "A importância da água para o corpo humano", "Os melhores aplicativos de viagem", "História das Olimpíadas Antigas",
    "Como construir um terrário?", "Os museus mais famosos do mundo", "Como aprender a cozinhar?", "As montanhas mais altas do planeta"
]

options = webdriver.EdgeOptions() #Cria opções de configuração para o navegador
driver = webdriver.Edge(options=options) #Abre o navegador Edge com as configurações definidas
    
try:
    for _ in range(3):  # Realiza 3 buscas aleatórias
        search_query = random.choice(search_terms)  # Escolhe um termo aleatório
        driver.get("https://www.google.com") #Acessa o site do Google
        search_box = driver.find_element(By.NAME, "q") #Encontra a caixa de busca do Google, localizando o elemento com o nome "q" (o nome usado pelo Google para o campo de pesquisa).
        search_box.send_keys(search_query) #Envia o termo de pesquisa escolhido para a caixa de pesquisa.
        search_box.send_keys(Keys.RETURN) #Simula pressionar a tecla Enter para submeter a busca.
        time.sleep(random.randint(5, 30))  # Aguarda um tempo aleatório entre 5 e 15 segundos


finally:
    driver.quit()
