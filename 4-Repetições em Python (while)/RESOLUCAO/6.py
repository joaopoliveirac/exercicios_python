# 6. Número de Dígitos de um Número
# Peça ao usuário um número inteiro e conte quantos dígitos ele tem usando while.

def contar_digitos():
    numero = int(input("Informe um número inteiro: "))
    numero = abs(numero)  # Garante que números negativos também sejam contados corretamente
    contador = 0

    if numero == 0:  
        return 1  # O número 0 tem 1 dígito

    while numero > 0:
        numero //= 10  # Remove o último dígito
        contador += 1

    return contador

print(f"Quantidade de dígitos: {contar_digitos()}")
