# 2. Número Primo
# Peça ao usuário um número e use while para verificar se ele é primo (divisível apenas por 1 e ele mesmo).

# Exemplo:
# Entrada: 13
# Saída: "13 é um número primo."

def eh_primo():
    numero = int(input("Informe um número inteiro positivo: "))

    if numero < 2:
        return f"{numero} não é um número primo."

    divisor = 2  # Começamos com o menor divisor possível
    while divisor * divisor <= numero:  # Verifica até a raiz quadrada do número
        if numero % divisor == 0:
            return f"{numero} não é um número primo."
        divisor += 1

    return f"{numero} é um número primo."

print(eh_primo())
