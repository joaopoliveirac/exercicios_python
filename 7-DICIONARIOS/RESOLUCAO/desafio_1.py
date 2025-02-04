# 1. Inverter um Dicionário
# Crie uma função que inverta um dicionário, trocando as chaves pelos valores.

def inverter_dicionario(dicionario):
    dicionario_novo = {}
    for chave,valor in dicionario.items():
        dicionario_novo[valor] = chave
    
    return dicionario_novo

dicionario = {'joao': 25, 'pedro': 50, 'jose': 70}
print(inverter_dicionario(dicionario))