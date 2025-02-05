# 4. Função que Retorna o Maior Número
# Crie uma função maior_numero(a, b, c) que retorna o maior número entre três números fornecidos como parâmetros.

def maior_numero(a,b,c):
    lista = [a,b,c]
    return max(lista)

print(maior_numero(9,3,7))