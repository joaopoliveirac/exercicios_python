# 9. Função de Contagem Regressiva
# Crie uma função contagem_regressiva(n) que recebe um número n e imprime os números de n até 1.

def contagem_regressiva(n):
    for i in range(n,0,-1):
        print(i)

contagem_regressiva(5)