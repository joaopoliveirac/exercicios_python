# 2-Obter Dados de um Repositório no GitHub
# Objetivo: Fazer uma requisição GET para a API do GitHub e obter informações sobre um repositório público, como https://api.github.com/repos/{owner}/{repo}.
# Dica: Escolha um repositório público e use a API para extrair informações como nome, descrição e número de estrelas.

import requests
owner = 'joaopoliveirac'
repo = 'Bootcamp-Ptyhon-para-dados'

response = requests.get(f'https://api.github.com/repos/{owner}/{repo}')
if response.status_code == 200:
    data = response.json()
    nome = data['name'] 
    descricao = data['description']
    estrelas = data.get('stargazers_count', 0) #retorna 0 se a chave nao existir
    print(nome,descricao,estrelas)