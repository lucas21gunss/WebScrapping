# Coleta de Dados do Clima de São Paulo

Este repositório contém dois scripts em Python para a coleta automatizada de dados meteorológicos da cidade de São Paulo, utilizando duas abordagens:

- **Web Scraping:** Coleta de dados diretamente do site [timeanddate.com](https://www.timeanddate.com/weather/brazil/sao-paulo) usando as bibliotecas `requests` e `BeautifulSoup`.
- **API:** Coleta de dados via API pública da [Open-Meteo](https://open-meteo.com/) utilizando a biblioteca `requests`.

Os dados coletados são salvos em arquivos CSV. Este projeto também inclui a documentação auxiliar e este README com instruções para instalação e execução dos scripts.

## Estrutura do Repositório


## Pré-requisitos

Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado na sua máquina.

## Instalação das Dependências

Abra o terminal (ou prompt de comando) e instale as bibliotecas necessárias utilizando o `pip`:

```bash
pip install requests beautifulsoup4
Instruções de Execução
1. Executar o Script de Web Scraping
Este script coleta dados diretamente do site e gera o arquivo weather_scraped.csv.

bash
Copiar
python script_webscraping.py
Após a execução, verifique a criação do arquivo weather_scraped.csv na pasta do projeto.

2. Executar o Script da API
Este script coleta dados do clima utilizando a API da Open-Meteo e gera o arquivo weather_api.csv.

bash
Copiar
python script_api.py
Após a execução, verifique a criação do arquivo weather_api.csv na pasta do projeto.
