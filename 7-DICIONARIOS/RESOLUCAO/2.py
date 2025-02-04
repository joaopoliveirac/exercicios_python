# 2. Acessar um Valor no Dicionário
# Dado o dicionário idades, peça ao usuário para digitar o nome de uma pessoa e exiba sua idade.

dicionario = {'joao' : 15, 'pedro': 25, 'jose': 57}
nomes = [chave for chave,valor in dicionario.items()]
nome = input(f'informe o nome que deseja consultar a idade, nomes disponiveis: \n {nomes}: ')
if nome in nomes:
    print(f'{nome} tem {dicionario[nome]} anos.')
else:
    print('esse ser nao ta aqui.')