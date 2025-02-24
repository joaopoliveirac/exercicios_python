# 1-Extração de Dados de uma API Pública (exemplo: JSONPlaceholder)
# Objetivo: Fazer uma requisição GET para a API JSONPlaceholder e exibir os dados de usuários (/users).
# Dica: Use a biblioteca requests para obter os dados e imprima os resultados.

import requests

r = requests.get('https://jsonplaceholder.typicode.com/users/1')
dados = r.json()
print(dados)
