# 2. Tabuada de um Número
# Peça ao usuário um número e exiba sua tabuada de 1 a 10 usando while.

def tabuada(numero):
    multiplicador = 1
    while multiplicador <= 10:
        print(multiplicador * numero)
        multiplicador += 1
    
numero = int(input('informe um numero: '))
tabuada(numero)