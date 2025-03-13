import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def get_game_details(self, game_url):
        try:
            self.driver.get(game_url)

            # Espera até que o nome do jogo esteja visível
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "entry-title"))
            )

            # Extrair os dados
            name = self.driver.find_element(By.CLASS_NAME, "entry-title").text
            image = self.driver.find_element(By.CLASS_NAME, "alignleft").get_attribute("src")
            
            # Buscando o link magnet corretamente, que sempre estará no formato href="magnet:..."
            magnet_elements = self.driver.find_elements(By.XPATH, "//a[contains(@href, 'magnet:')]")
            magnet = magnet_elements[0].get_attribute("href") if magnet_elements else None

            # Retorna os dados coletados
            return {
                "name": name,
                "image": image,
                "url": magnet
            }

        except Exception as e:
            print(f"Erro ao coletar detalhes do jogo: {game_url} - {str(e)}")
            return None

    def process_game_urls(self, urls_file, output_file):
        all_game_data = []

        try:
            # Lê as URLs do arquivo urls.txt
            with open(urls_file, 'r', encoding='utf-8') as file:
                game_urls = file.readlines()

            # Verifica se o arquivo JSON já existe, caso contrário, cria um novo
            try:
                with open(output_file, 'r', encoding='utf-8') as json_file:
                    all_game_data = json.load(json_file)  # Carrega os dados já existentes
            except FileNotFoundError:
                pass  # Se o arquivo não existir, começa com uma lista vazia

            # Processa cada URL
            for game_url in game_urls:
                game_url = game_url.strip()  # Remove espaços em branco extras
                if game_url:
                    game_data = self.get_game_details(game_url)
                    if game_data:
                        all_game_data.append(game_data)
                        print(f"Informações do jogo {game_data['name']} salvas em tempo real.")

                        # Salva os dados imediatamente após coletá-los
                        with open(output_file, 'w', encoding='utf-8') as json_file:
                            json.dump(all_game_data, json_file, ensure_ascii=False, indent=4)

            print(f"Todos os dados dos jogos foram salvos em {output_file}.")

        except Exception as e:
            print(f"Erro ao processar as URLs: {str(e)}")


# Chama a função para salvar os dados dos jogos em um arquivo JSON, passando a lista de URLs
if __name__ == "__main__":
    fitgirl = FitGirl()
    fitgirl.process_game_urls('urls.txt', 'lista.json')
