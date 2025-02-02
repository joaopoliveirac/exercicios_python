# 1. Jogo de Adivinhação com Tentativas Limitadas
# Crie um jogo onde o usuário tem 5 tentativas para adivinhar um número entre 1 e 50.

# Exemplo:
# Entrada: 10 (tentativa errada)
# Entrada: 25 (tentativa errada)
# Entrada: 33 (acertou!)
# Saída: "Parabéns! Você acertou em 3 tentativas."
from random import randint

def jogo_advinhacao():
    numero_aleatorio = randint(1,50)
    tentativas = 0
    while True:
        if tentativas < 5:
            numero = int(input('Informe o numero para tentar acertar: '))
            if numero != numero_aleatorio:
                print('Tentativa errada.')
            else:
                print('Voce acertou!!')
                break
            tentativas += 1
        else:
            break
    return 'Voce não conseguiu acertar.'

print(jogo_advinhacao())