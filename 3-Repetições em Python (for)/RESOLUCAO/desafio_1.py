# 1. Número Perfeito
# Um número perfeito é aquele cuja soma dos seus divisores (exceto ele mesmo) é igual ao próprio número.

# Peça ao usuário um número e verifique se ele é perfeito.

# Exemplo:
# Entrada: 6
# Divisores: 1, 2, 3
# Soma: 1 + 2 + 3 = 6
# Saída: "6 é um número perfeito"


def eh_numero_perfeito(n):
    soma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return soma_divisores == n

numero = int(input("Digite um número: "))

if eh_numero_perfeito(numero):
    print(f"{numero} é um número perfeito!")
else:
    print(f"{numero} não é um número perfeito.")

