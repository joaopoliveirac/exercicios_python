# 5. Agrupar Itens de uma Lista em um Dicionário
# Dada uma lista de tuplas, agrupe as tuplas por chaves e crie um dicionário onde as chaves sejam o primeiro elemento de cada tupla e os valores sejam listas com os segundos elementos.

def agrupar_itens(lista):
    dicionario = {}
    for tupla in lista:
        if tupla[0] in dicionario:
            dicionario[tupla[0]] += [tupla[1]]
        else:
            dicionario[tupla[0]] = [tupla[1]]
    return dicionario
    
produtos = [
    ("Notebook", 3500.00),
    ("Mouse", 80.00),
    ("Teclado", 150.00),
    ("Monitor", 1200.00),
    ("Cabo USB", 30.00)
]

for chave, valor,teste in produtos:
    print(chave)
    print(valor)
    print(teste)
print(agrupar_itens(produtos))



from collections import defaultdict

def agrupar_itens(lista: list[tuple[str, float]]) -> dict[str, list[float]]:
    dicionario = defaultdict(list)
    
    for chave, valor in lista:
        dicionario[chave].append(valor)
    
    return dict(dicionario)  # Convertendo para um dicionário normal
