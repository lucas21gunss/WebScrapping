#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script 2: Coleta de dados meteorológicos via API (Open-Meteo).
Consulta a API para obter o clima atual de São Paulo e gera um CSV.
"""

import requests
import csv
import sys

# Mapeamento dos códigos de clima para descrições amigáveis.
WEATHER_CODE_MAP = {
    0: "Céu limpo",
    1: "Predominantemente limpo",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Neblina",
    48: "Neblina com geada",
    51: "Chuvisco leve",
    53: "Chuvisco moderado",
    55: "Chuvisco denso",
    56: "Chuvisco congelante leve",
    57: "Chuvisco congelante denso",
    61: "Chuva leve",
    63: "Chuva moderada",
    65: "Chuva forte",
    66: "Chuva congelante leve",
    67: "Chuva congelante forte",
    71: "Queda de neve leve",
    73: "Queda de neve moderada",
    75: "Queda de neve intensa",
    77: "Grãos de neve",
    80: "Borrasca de chuva leve",
    81: "Borrasca de chuva moderada",
    82: "Borrasca de chuva violenta",
    85: "Borrasca de neve leve",
    86: "Borrasca de neve intensa",
    95: "Trovoada",
    96: "Trovoada com granizo leve",
    99: "Trovoada com granizo forte"
}

def coletar_dados_api():
    # Coordenadas de São Paulo.
    latitude = -23.5505
    longitude = -46.6333

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": "true"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro na requisição à API: {e}")
        sys.exit(1)

    dados = response.json()

    if "current_weather" not in dados:
        print("Dados de clima atuais não foram retornados pela API.")
        sys.exit(1)

    clima_atual = dados["current_weather"]
    temperatura = clima_atual.get("temperature", "N/D")
    weathercode = clima_atual.get("weathercode", None)
    condicao = WEATHER_CODE_MAP.get(weathercode, "Indefinido")
    hora = clima_atual.get("time", "N/D")

    return {
        "Cidade": "São Paulo",
        "Temperatura": f"{temperatura}°C",
        "Condição": condicao,
        "Hora": hora,
        "Fonte": "API Open-Meteo"
    }

def salvar_csv(dados, nome_arquivo="weather_api.csv"):
    campos = ["Cidade", "Temperatura", "Condição", "Hora", "Fonte"]
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=campos)
            writer.writeheader()
            writer.writerow(dados)
        print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

if __name__ == '__main__':
    dados_clima_api = coletar_dados_api()
    salvar_csv(dados_clima_api)
