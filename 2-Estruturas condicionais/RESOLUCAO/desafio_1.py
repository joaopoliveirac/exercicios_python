# 1. Simulador de Caixa Eletrônico
# Peça ao usuário um valor de saque e determine quantas cédulas de 100, 50, 20, 10 e 5 são necessárias para pagar esse valor.

def caixa_eletronico(valor):
    lista = []
    if valor < 5:
        return 'valor invalido para saque'
    if valor >= 100:
        notas_100 = int(valor / 100)
        lista.append(f'{notas_100} notas de 100')
        valor = valor - (notas_100 * 100)
    if valor >= 50:
        notas_50 = int(valor / 50)
        valor = valor - (notas_50 * 50)
        lista.append(f'{notas_50} notas de 50')
    if valor >= 20:
        notas_20 = int(valor / 20)
        valor = valor - (notas_20 * 20)
        lista.append(f'{notas_20} notas de 20')
    if valor >= 10:
        notas_10 = int(valor / 10)
        valor = valor - (notas_10 * 10)
        lista.append(f'{notas_10} notas de 10')
    if valor >= 5:
        notas_5 = int(valor / 5)
        valor = valor - (notas_5 * 5)
        lista.append(f'{notas_5} notas de 5.')
    return ', '.join(lista)

valor = int(input('informe o valor: '))
print(caixa_eletronico(valor))



#GPTECO ME DEU, não tinha pensado dessa maneira. me compliquei em cima atoa.
def caixa_eletronico(valor):
    if valor < 5:
        return 'Não sacamos abaixo de 5 reais.'
    cedulas = [100,50,20,10,5]
    notas = []

    for cedula in cedulas:
        quantidade_de_notas = valor // cedula #o resultado é apenas a parte inteira, ele descarta o decimal.
        if quantidade_de_notas > 0:
            notas.append(f'{quantidade_de_notas} notas de {cedula} reais')
            valor -= quantidade_de_notas * cedula #atualizar o valor restante
    return ', '.join(notas)

valor = int(input('Informe o valor do saque: '))
print(caixa_eletronico(valor))

    
    
