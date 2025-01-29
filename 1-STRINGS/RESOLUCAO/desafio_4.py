# 4. Compactação de String
# Implemente um algoritmo que compacte uma string substituindo sequências repetidas de caracteres pelo caractere seguido da quantidade de repetições.






def compacter_string(texto):
    resultado = []
    contador = 1 
    for i in range(1,len(texto)):
        if texto[i] == texto[i-1]:
            contador += 1
        else:
            resultado.append(texto[i-1] + str(contador))
            contador = 1
    resultado.append(texto[-1] + str(contador))
    return ''.join(resultado)

entrada = 'aaaabbbbbbccccc'
print(compacter_string(entrada))
