# 4-Consultar Preços de Criptomoedas com a CoinGecko API
# Objetivo: Acesse a API pública da CoinGecko e extraia informações sobre o preço de criptomoedas, como o Bitcoin.
# Dica: Use https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd para obter o preço do Bitcoin em USD.

import requests

url = 'https://api.coingecko.com/api/v3/coins/list'
response = requests.get(url)
dados = response.json()

for lista in dados: #fiz esse for apenas para pratica..
    if lista['id'] == 'bitcoin' and lista['symbol'] == 'btc':
        bitcoin = lista

#print(bitcoin)
id = bitcoin['id']
moeda = 'usd'
url_preco = f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies={moeda}'
response_preco = requests.get(url_preco)
dados_moeda = response_preco.json()
valor = dados_moeda[id][moeda]
print(f'O {id} está custando {valor} {moeda}.')