# 4. Função que Verifica se um Número é Primo
# Crie uma função verifica_primo(n) que recebe um número n e retorna True se ele for primo 
# (divisível apenas por 1 e por ele mesmo) e False caso contrário.



import math

def verifica_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Testa até a raiz quadrada de n
        if n % i == 0:
            return False
    return True

# Testes
print(verifica_primo(7))   # True
print(verifica_primo(10))  # False
print(verifica_primo(29))  # True
print(verifica_primo(1))   # False
