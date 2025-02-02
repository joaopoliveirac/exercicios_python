# 7. Fatorial de um Número
# Peça ao usuário um número e calcule seu fatorial usando while.

def calcular_fatorial():
    numero = int(input('informe um numero: '))
    multiplicador = numero -1
    resultado = numero * multiplicador
    while multiplicador > 1:
        multiplicador -= 1
        resultado = resultado * multiplicador
    return resultado

print(calcular_fatorial())
