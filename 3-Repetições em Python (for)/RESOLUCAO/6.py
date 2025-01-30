# 6. Fatorial de um Número
# Peça ao usuário um número e calcule o fatorial usando um for.
numero = int(input('informe o numero para calcular o fatorial: '))
resultado = numero
for i in range(numero -1 , 0, -1):
    resultado *= i

print(resultado)


