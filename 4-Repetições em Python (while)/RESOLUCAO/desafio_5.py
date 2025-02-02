# 5. Sequência de Collatz
# Peça ao usuário um número e aplique a Sequência de Collatz até chegar a 1.

# Regras:

# Se o número for par, divida por 2.
# Se for ímpar, multiplique por 3 e some 1.


def sequencia_collatz():
    numero = int(input("Informe um número inteiro positivo: "))

    if numero <= 0:
        return "O número deve ser maior que zero."

    print(f"Sequência de Collatz para {numero}:")
    
    while numero != 1:
        print(numero, end=" → ")  # Exibe o número atual
        if numero % 2 == 0:  # Se for par, divide por 2
            numero //= 2
        else:  # Se for ímpar, multiplica por 3 e soma 1
            numero = (numero * 3) + 1

    print(1)  # Exibe o último número da sequência

print(sequencia_collatz())
