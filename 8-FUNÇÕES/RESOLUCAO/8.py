# 8. Função de Fatorial
# Crie uma função fatorial(n) que calcula o fatorial de um número n.

def calcular_fatorial(numero):
    resultado = numero
    for i in range(numero -1 , 0, -1):
        resultado *= i
    return resultado


numero = int(input('informe o numero para calcular o fatorial: '))
print(calcular_fatorial(numero))