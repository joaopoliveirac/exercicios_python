# 10. Desenhar um Triângulo de Asteriscos
# Peça ao usuário um número N e exiba um triângulo de altura N usando *.

# Solicita ao usuário um número inteiro
N = int(input("Digite a altura do triângulo: "))

# Loop para criar o triângulo
for i in range(1, N + 1):
    print("*" * i)  # Multiplica o caractere "*" pelo valor de i
