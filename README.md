# FitGirl Repacks Scraper

Este repositório contém dois scripts Python para coleta de informações de jogos do site **FitGirl Repacks**. O primeiro script (`list.py`) coleta URLs de jogos e as salva em um arquivo de texto, enquanto o segundo script (`games.py`) coleta detalhes de cada jogo listado, como nome, imagem de capa e link Magnet, salvando-os em um arquivo JSON.

## Requisitos

Antes de rodar os scripts, é necessário garantir que você tenha os seguintes requisitos instalados:

- **Python 3.x**: Certifique-se de ter o Python instalado no seu sistema.
- **Selenium**: O Selenium é utilizado para controlar o navegador.
  - Para instalar o Selenium, execute:
    ```bash
    pip install selenium
    ```
- **ChromeDriver**: O [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) é necessário para controlar o navegador Chrome (ou Brave) via Selenium. Baixe a versão compatível com a sua versão do navegador e coloque o arquivo na mesma pasta do script ou especifique o caminho no código.
- **Brave Browser**: Caso queira usar o navegador Brave, certifique-se de tê-lo instalado no seu sistema. Você pode modificar o código para usar o Google Chrome também.

## Funcionalidade dos Scripts

### 1. **list.py** - Coleta URLs de Jogos

Esse script percorre as páginas do site **FitGirl Repacks** e coleta as URLs dos jogos, salvando-as em um arquivo de texto chamado `game_urls.txt`.

- **Como funciona**:
  - O script navega pelas páginas do site (de 1 até 108) e coleta os links dos jogos.
  - Esses links são extraídos e salvos em `game_urls.txt`.
  - Ele usa o Selenium para controlar o navegador e navegar pelas páginas.

### 2. **games.py** - Coleta Detalhes de Cada Jogo

Esse script coleta detalhes de cada jogo listado no arquivo `game_urls.txt`, como nome, imagem de capa e link Magnet, e salva essas informações em um arquivo JSON (`lista.json`).

- **Como funciona**:
  - O script lê as URLs dos jogos de `game_urls.txt`.
  - Para cada URL, ele coleta o nome do jogo, a imagem de capa e o link Magnet.
  - As informações coletadas são salvas em tempo real no arquivo `lista.json`.

## Como Rodar os Scripts

### Passo 1: Baixar os Arquivos Necessários
- Baixe o **ChromeDriver** ou **BraveDriver** (dependendo do navegador escolhido) e coloque-o na mesma pasta dos scripts ou altere o caminho no código.
- Instale o Selenium:
  ```bash
  pip install selenium

## Passo 2: Rodar os Scripts

### Executar `list.py`

Para começar a coletar as URLs dos jogos, execute o script `list.py`. Esse script navega pelas páginas do site **FitGirl Repacks** e salva as URLs dos jogos no arquivo `game_urls.txt`.

## Execute o seguinte comando:
```bash
python list.py
```


### Após a execução, as URLs dos jogos estarão disponíveis no arquivo game_urls.txt.

 - Executar games.py
- Para coletar os detalhes de cada jogo (como nome, imagem de capa e link Magnet), execute o script games.py. Esse script lê as URLs do arquivo game_urls.txt, acessa cada uma delas e salva as informações coletadas no arquivo lista.json.
- Execute o seguinte comando:
```bash
python list.py
