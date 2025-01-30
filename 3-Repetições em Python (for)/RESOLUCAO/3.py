# 3. Soma dos Primeiros N Números
# Peça um número ao usuário e calcule a soma dos primeiros N números naturais.

numero = int(input('informe um numero'))
soma = 0

for i in range (0,numero):
    soma += i

print(soma)
