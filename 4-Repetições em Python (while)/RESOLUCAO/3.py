# 3. Número Secreto
# Crie um programa que sorteia um número de 1 a 100 e peça ao usuário para adivinhar. O programa continua executando até que o usuário acerte.

from random import randint

def numero_secreto():
    aleatorio = randint(1,100)
    numero = None
    while numero != aleatorio:
        numero = int(input('informe um numero de 1 a 100: '))
        print("NUMERO DIFERENTE")
    return 'ACERTOU'

print(numero_secreto())