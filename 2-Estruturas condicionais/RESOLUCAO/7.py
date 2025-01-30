# 7. Números em Ordem Crescente
# Peça três números ao usuário e exiba-os em ordem crescente.

def ordenar_numeros(n1,n2,n3):
    numeros = [n1,n2,n3]
    return sorted(numeros)

n1 = float(input('infomre o primeiro numero'))
n2 = float(input('informe o segundo numero'))
n3 = float(input('informe o terceiro numero'))

resultado = ordenar_numeros(n1,n2,n3)
print(resultado)
