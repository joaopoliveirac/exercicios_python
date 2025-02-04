# 5. Verificar Existência de uma Chave
# Dado o dicionário idades, verifique se a chave "João" existe.

dicionario = {'joao' : 15, 'pedro': 25, 'jose': 57, 'carlos' : 55}
if 'joao' in dicionario:
    print(f' Joao existe e tem {dicionario['joao']} anos.')
else:
    print('nao existe.') 