# 8. Números Primos até N
# Peça ao usuário um número N e exiba todos os números primos até N.

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Verifica até a raiz quadrada de n
        if n % i == 0:  # Se n for divisível por i, não é primo
            return False
    return True  # Se não for divisível por nenhum número, é primo

# Exemplo de uso
numero = int(input("Digite um número para verificar se é primo: "))
if is_prime(numero):
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo!")
