# 3. Dicionário de Frequência de Palavras
# Crie um dicionário que conta a frequência de palavras em uma lista de palavras.

def contar_frequencia(lista):
    dicionario ={}
    for palavra in lista:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    return dicionario

lista = ['joao','joao', 'jose','oliveira','jose','oliveira']
print(contar_frequencia(lista))


from collections import Counter

def contar_frequencia_01(lista):
    return dict(Counter(lista))

print(contar_frequencia_01(lista))