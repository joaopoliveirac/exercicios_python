# 6. Classificação de Triângulos
# Peça ao usuário três lados de um triângulo e informe se ele é equilátero, isósceles ou escaleno.

def triangulo(l1,l2,l3):
    if l1 == l2 == l3:
        return 'triangulo equilatero'
    elif l1 != l2 and l1 != l3 and l2 != l3:
        return 'triangulo escaleno'
    else:
        return 'triangulo isosceles'
    

l1 = float('informe o primeiro lado')
l2 = float('informe o segundo lado')
l3 = float('informe o terceiro lado')

triangulo(l1,l2,l3)