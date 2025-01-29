# 2. Maior de Dois Números
# Peça dois números ao usuário e exiba o maior.

def numero_maior(n1,n2):
    if n1 > n2:
        print('o primeiro número é o maior.')
    else:
        print('o segundo número é o maior.')

n1 = int(input('informe o primeiro numero: '))
n2= int(input('informe o segundo numero'))

numero_maior(n1,n2)