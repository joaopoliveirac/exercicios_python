# 1. Função Recursiva de Fatorial
# Crie uma função recursiva fatorial(n) para calcular o fatorial de um número n (sem usar loops).

def calcular_fatorial(n):
    if n == 0:
        return 1
    return n * calcular_fatorial(n - 1)

print(calcular_fatorial(5))