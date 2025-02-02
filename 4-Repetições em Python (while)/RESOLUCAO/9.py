# 9. Sequência de Fibonacci (até N termos)
# Peça ao usuário um número N e exiba os primeiros N números da sequência de Fibonacci usando while.

def fibonacci_n_termos():
    N = int(input("Informe um número N para a sequência de Fibonacci: "))

    if N <= 0:
        print("Por favor, informe um número maior que zero.")
        return

    a, b = 0, 1  # Dois primeiros números da sequência
    contador = 0

    while contador < N:
        print(a, end=" ")  # Exibe o número atual da sequência
        a, b = b, a + b  # Atualiza os valores para o próximo termo
        contador += 1  # Incrementa o contador

print(fibonacci_n_termos())
