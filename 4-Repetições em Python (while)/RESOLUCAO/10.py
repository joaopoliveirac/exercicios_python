# 10. Inverter um Número
# Peça ao usuário um número inteiro e exiba ele invertido usando while.

def inverter_numero():
    while True:
        numero = int(input('informe um numero: '))
        numero = str(numero)
        if type(numero) == str:
            break
    return numero[::-1]

print(inverter_numero())