# 2. Contar Ocorrências de Elementos em uma Lista de Dicionários
# Dada uma lista de dicionários com nomes e idades, crie um dicionário que conte quantas vezes cada idade aparece na lista.

lista_de_dicionarios = [
    {'nome': 'João', 'idade': 25},
    {'nome': 'Maria', 'idade': 22},
    {'nome': 'Carlos', 'idade': 22},
    {'nome': 'Ana', 'idade': 28},
    {'nome': 'Pedro', 'idade': 35}
]

dicionario = {}

for i in lista_de_dicionarios:
    for chave,valor in i.items():
        if chave == 'idade':
            if valor in dicionario:
                dicionario[valor] += 1
            else:
                dicionario[valor] = 1

print(dicionario)
