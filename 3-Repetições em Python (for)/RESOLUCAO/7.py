def fibonacci(n):
    a, b = 0, 1
    sequencia = []
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

n = int(input("Digite o número de termos da sequência de Fibonacci: "))
print(f"Os primeiros {n} números da sequência de Fibonacci são: {fibonacci(n)}")
