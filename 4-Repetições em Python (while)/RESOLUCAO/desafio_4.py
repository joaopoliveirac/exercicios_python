# 4. Palíndromo Numérico
# Peça ao usuário um número e verifique se ele é um palíndromo (igual quando lido de trás para frente).

# Exemplo:
# Entrada: 12321
# Saída: "O número é um palíndromo."

def verificar_palindromo():
    numero = int(input("Informe um número inteiro: "))
    numero_original = numero  # Guarda o número original para comparar depois
    invertido = 0  

    while numero > 0:
        ultimo_digito = numero % 10  # Obtém o último dígito
        invertido = (invertido * 10) + ultimo_digito  # Constrói o número invertido
        numero //= 10  # Remove o último dígito do número original

    if numero_original == invertido:
        return "O número é um palíndromo."
    else:
        return "O número não é um palíndromo."

print(verificar_palindromo())
