from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

BASE_URL = "https://fitgirl-repacks.site/all-my-repacks-a-z/?lcp_page0={page_num}#lcp_instance_0"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
CHROMEDRIVER_PATH = "./chromedriver.exe"

class FitGirl:
    def __init__(self):
        options = Options()
        options.binary_location = BRAVE_PATH
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Remove "--headless" para visualizar o navegador e depurar
        # options.add_argument("--headless")

        # Simula um usuário real com User-Agent
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.45 Safari/537.36")

        self.driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)

    def get_urls_from_page(self, page_num):
        try:
            # Formatar o link da página
            url = BASE_URL.format(page_num=page_num)
            self.driver.get(url)

            # Espera até que a página carregue e ao menos um link esteja visível
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "a"))
            )

            # Coleta todos os links da página
            links = self.driver.find_elements(By.TAG_NAME, "a")
            
            # Filtra os links que começam com https://fitgirl-repacks.site/
            game_urls = [link.get_attribute("href") for link in links if link.get_attribute("href") and link.get_attribute("href").startswith("https://fitgirl-repacks.site/")]

            return game_urls

        except Exception as e:
            print(f"Erro ao processar a página {page_num}: {str(e)}")
            return []

    def save_game_urls_to_file(self):
        try:
            with open('game_urls.txt', 'a') as file:  # Abre o arquivo no modo de append ('a')
                for page_num in range(1, 109):  # Vai de 1 até 108
                    game_urls = self.get_urls_from_page(page_num)

                    # Se encontrou URLs, escreve no arquivo
                    if game_urls:
                        for url in game_urls:
                            file.write(url + '\n')  # Escreve cada URL em uma nova linha
                        print(f"URLs da página {page_num} salvas em tempo real.")
                    else:
                        print(f"Nenhuma URL encontrada na página {page_num}.")

        except Exception as e:
            print(f"Erro ao salvar as URLs: {str(e)}")

# Chama a função para salvar as URLs dos jogos em um arquivo
if __name__ == "__main__":
    fitgirl = FitGirl()
    fitgirl.save_game_urls_to_file()
