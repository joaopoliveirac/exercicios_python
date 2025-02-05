# 5. Função que Realiza um Desafio de Jogo de Adivinhação
# Crie uma função adivinha_numero() que sorteia um número aleatório entre 1 e 100, e o usuário tem que adivinhar o número. 
# A função deve retornar "Muito alto", "Muito baixo" ou "Acertou!" dependendo do valor da tentativa. 
# O jogo continua até o número ser adivinhado.

from random import randint

def adivinha_numero():
    aleatorio = randint(1, 100)  # O número sorteado deve estar entre 1 e 100
    numero = None  # Inicializa a variável
    
    while numero != aleatorio:
        try:
            numero = int(input("Informe um número de 1 a 100: "))  # Garante que a entrada seja um número inteiro
            if numero < 1 or numero > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue  # Volta para a próxima iteração do loop
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
            continue  # Volta para a próxima iteração do loop

        if numero < aleatorio:
            print("Muito baixo.")
        elif numero > aleatorio:
            print("Muito alto.")

    return f"Acertou! O número era {aleatorio}."

# Chama a função
print(adivinha_numero())
