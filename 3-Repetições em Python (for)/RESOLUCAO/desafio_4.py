# 4. Matriz Identidade
# Peça ao usuário um número N e gere uma matriz identidade de ordem N × N.


def matriz_identidade(n):
    identidade = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    return identidade

# Solicita ao usuário um número inteiro
N = int(input("Digite o valor de N para a matriz identidade: "))

# Gera e imprime a matriz identidade
matriz = matriz_identidade(N)
for linha in matriz:
    print(linha)
