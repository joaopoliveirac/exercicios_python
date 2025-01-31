# 9. Inverter uma Palavra
# Peça ao usuário uma palavra e a exiba de trás para frente, utilizando for.

def inverter_palavra(palavra):
    nova_palavra = ''
    for i in range(-1,-(len(palavra)) -1,-1):
        nova_palavra += str(palavra[i])
    return nova_palavra


print(inverter_palavra('joao'))




