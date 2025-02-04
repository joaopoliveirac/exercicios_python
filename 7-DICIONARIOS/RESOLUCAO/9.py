# 9. Ordenar um Dicionário por Valores
# Dado um dicionário com números como valores, ordene-o em ordem crescente.

dicionario = {'brasil' : 4565465, 'frança': 454545465, 'japao' : 546465449898 , 'eua': 787798}
dicionario_ordenado = dict(sorted(dicionario.items(), key=lambda item: item[1]))
print(dicionario_ordenado)