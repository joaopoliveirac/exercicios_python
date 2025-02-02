# 3. Conversor de Número para Binário
# Peça ao usuário um número decimal e converta para binário usando while.

# Exemplo:
# Entrada: 10
# Saída: "1010"


def converter_para_binario():
    numero = int(input("Informe um número decimal: "))

    if numero == 0:
        return "0"

    binario = ""
    while numero > 0:
        resto = numero % 2  # Pega o resto da divisão por 2
        binario = str(resto) + binario  # Adiciona o bit à esquerda
        numero //= 2  # Divide o número por 2 para continuar a conversão

    return binario

print(f"Binário: {converter_para_binario()}")
