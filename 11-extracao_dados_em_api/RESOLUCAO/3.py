# 3-Extração de Dados Climáticos com a API OpenWeatherMap
# Objetivo: Utilizar a OpenWeatherMap API para obter o clima de uma cidade específica.
# Dica: Inscreva-se para uma chave de API gratuita e use a API para obter dados como temperatura, umidade e condições climáticas.

import requests
from datetime import datetime,timedelta,timezone
#obtendo os dados de lat e lon para depois achar a temperatura
zip_code = '38270000'
country_code = 'BR'
api_key = "5b567037bebc4cbe1375a31b443a0485"
url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
response = requests.get(url)
dados = response.json()
nome_cidade = dados.get('name')
lat = dados.get('lat')
lon = dados.get('lon')
#agora vamos obter as informações solicitadas, temp, umidade etc
url_1 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
response_final = requests.get(url_1)
dados_final = response_final.json()
#pegando as temp solicitadas.
dados_temperatura = dados_final['main']
temperatura_atual = dados_temperatura['temp']
temperatura_minima = dados_temperatura['temp_min']
temperatura_maxima = dados_temperatura['temp_max']
umidade = dados_temperatura['humidity']
print(f'Temperatura minima: {temperatura_minima}. Temperatura Maxima: {temperatura_maxima}. Temperatura atual: {temperatura_atual}. Umidade: {umidade}')
def converter_timestamp(timestamp, timezone_offset):
    # Ajuste do timezone com a quantidade de horas de diferença em horas (timezone_offset)
    tz = timezone(timedelta(seconds=timezone_offset))  # Convertendo a diferença de segundos para horas
    return datetime.fromtimestamp(timestamp, tz).strftime('%H:%M:%S')

#convertendo os horarios
hora_atual = converter_timestamp(dados_final['dt'], dados_final['timezone'])
print(hora_atual)