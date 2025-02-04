# 8. Obter Todas as Chaves e Valores
# Crie um dicionário e exiba todas as chaves e valores em listas separadas.

dicionario = {'brasil' : 4565465, 'frança': 454545465, 'japao' : 546465449898 , 'eua': 787798}
paises = [chave for chave, valor in dicionario.items()]
populacao = [valor for chave,valor in dicionario.items()]
print(paises)
print(populacao)


#ou

paises = list(dicionario.keys())
populacao = list(dicionario.values())
print(paises)
print(populacao)
