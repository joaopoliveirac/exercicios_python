# 5. Cálculo do Número de Dígitos de um Fatorial
# Peça ao usuário um número N e calcule quantos dígitos tem o número N! sem calcular o fatorial diretamente.

# Dica: Utilize logaritmos para encontrar o número de dígitos.

# Exemplo:
# Entrada: 10!
# Saída: 7 dígitos (pois 10! = 3.628.800 tem 7 dígitos)


import math

def num_digitos_fatorial(n):
    if n == 0 or n == 1:
        return 1  # 0! e 1! têm apenas 1 dígito (1)
    
    # Soma dos logaritmos para calcular log10(N!)
    soma_logs = sum(math.log10(i) for i in range(1, n + 1))
    
    # Número de dígitos = parte inteira do log + 1
    return math.floor(soma_logs) + 1

# Solicita o número ao usuário
N = int(input("Digite um número N para calcular quantos dígitos tem N!: "))

# Calcula e exibe o resultado
print(f"O fatorial de {N} tem {num_digitos_fatorial(N)} dígitos.")
