# 5. Função que Realiza um Desafio de Jogo de Adivinhação
# Crie uma função adivinha_numero() que sorteia um número aleatório entre 1 e 100, e o usuário tem que adivinhar o número. 
# A função deve retornar "Muito alto", "Muito baixo" ou "Acertou!" dependendo do valor da tentativa. 
# O jogo continua até o número ser adivinhado.

from random import randint

def adivinha_numero():
    numero = None
    aleatorio = randint(1,100)
    while numero != aleatorio:
        try:
            numero = int(input('informe um numero de 1 a 100 até acerta: '))
        except ValueError:
            print('Digite um numero inteiro de 1 a 100.')
            continue
        if numero < aleatorio:
            print('numero muito baixo.')
        elif numero > aleatorio:
            print('numero muito alto.')
    return f'Voce acerto! O numero era {aleatorio} e voce digitou o {numero}.'
        
print(adivinha_numero())