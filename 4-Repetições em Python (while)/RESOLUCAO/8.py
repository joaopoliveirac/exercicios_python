# 8. Média de Números Positivos
# Peça ao usuário vários números positivos e calcule a média. O programa deve parar quando o usuário digitar um número negativo.

def calcular_media():
    numero = int(input('informe um numero positivo: '))
    soma = 0
    qtde_numero = 0
    while numero >= 0: 
        soma += numero
        qtde_numero += 1
        numero = int(input('informe um numero positivo: '))
    return soma / qtde_numero


print(calcular_media())
