# 4. Filtrar um Dicionário com Base no Valor
# Dado um dicionário de produtos com preços, crie um novo dicionário que contenha apenas os produtos com preços acima de 50.

def filtrar_valores(dicionario):
    dicionario_filtrado = {}
    for produto in dicionario:
        if dicionario[produto] > 50:
            dicionario_filtrado[produto] = dicionario[produto]
    return dicionario_filtrado


produtos = {
    "Notebook": 3500.00,
    "Mouse": 20.00,
    "Teclado": 40.00,
    "Monitor": 1200.00,
    "Impressora": 800.00
}



print(filtrar_valores(produtos))


def filtrar_valores_01(dicionario):
    dicionario_filtrado = {produto: preco for produto,preco in dicionario.items() if preco > 50}
    return dicionario_filtrado

print(filtrar_valores_01(produtos))