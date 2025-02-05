# 3. Função que Gera uma Sequência de Fibonacci
# Crie uma função fibonacci(n) que retorna a sequência de Fibonacci até o n-ésimo número. 
# A sequência começa com 0 e 1, e os próximos números são a soma dos dois anteriores.

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequencia = [0, 1]  # Inicializa a sequência com os dois primeiros números
    for _ in range(2, n):  
        sequencia.append(sequencia[-1] + sequencia[-2])  # Soma os dois últimos elementos
    return sequencia

# Teste da função
print(fibonacci(10))  
