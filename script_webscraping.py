
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script 1: Web Scraping para coleta de dados meteorológicos de São Paulo.
Utiliza as bibliotecas requests e BeautifulSoup para extrair os dados
da página https://www.timeanddate.com/weather/brazil/sao-paulo e gera um CSV.
"""

import requests
from bs4 import BeautifulSoup
import csv
import sys

def coletar_dados():
    url = 'https://www.timeanddate.com/weather/brazil/sao-paulo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'html.parser')

    # Procurando a seção do clima na página.
    clima_div = soup.find('div', id='qlook')
    if not clima_div:
        print("Não foi possível encontrar os dados do clima na página.")
        sys.exit(1)

    # Extraindo a temperatura.
    temp_element = clima_div.find('div', class_='h2')
    if temp_element:
        temperatura = temp_element.get_text(strip=True)
    else:
        temperatura = "N/D"

    # Extraindo a descrição do clima.
    desc_element = clima_div.find('p')
    if desc_element:
        condicao = desc_element.get_text(strip=True)
    else:
        condicao = "N/D"

    return {
        "Cidade": "São Paulo",
        "Temperatura": temperatura,
        "Condição": condicao,
        "Fonte": "Web Scraping"
    }

def salvar_csv(dados, nome_arquivo="weather_scraped.csv"):
    campos = ["Cidade", "Temperatura", "Condição", "Fonte"]
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            writer.writerow(dados)
        print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

if __name__ == '__main__':
    dados_clima = coletar_dados()
    salvar_csv(dados_clima)