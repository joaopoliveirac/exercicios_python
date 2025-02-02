# 4. Soma dos Primeiros N Números
# Peça um número ao usuário e use while para calcular a soma dos primeiros N números naturais.

def calcular_primeiros_n():
    numero = int(input('informe um numero'))
    numero_somar = 0
    soma = 0
    while numero_somar <= numero:
        soma += numero_somar
        numero_somar += 1
    return soma

print(calcular_primeiros_n())

