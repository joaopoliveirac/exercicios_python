# 10. Desconto no Valor da Compra
# Peça ao usuário o valor da compra e aplique um desconto:

def desconto_compra(valor,desconto):
    valor_final = valor * (1 - desconto)
    return valor_final

valor_compra = float(input('informe o valor da compra: '))

if valor_compra < 1000:
    valor = desconto_compra(valor_compra, 0.10)
elif 1000 < valor_compra < 2000:
    valor = desconto_compra(valor_compra, 0.20)
else:
    valor = desconto_compra(valor_compra, 0.30)

print(f'O valor final é {valor}')

