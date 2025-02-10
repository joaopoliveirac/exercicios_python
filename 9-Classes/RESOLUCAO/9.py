# 9-Classe Fila com estrutura de dados
# Crie uma classe Fila para simular uma estrutura FIFO (First-In, First-Out), 
# utilizando uma lista interna e métodos adicionar() e remover().

class Fila:
    def __init__(self):
        self.lista = []
        
    def adicionar(self,elemento):
        self.lista.append(elemento)
        return f'elemento {elemento} adicionado'
    
    def remover(self):
        if self.lista:
            return f'{self.lista.pop(0)} removido'
        else:
            return 'erro: a fila está vazia.'
        
fila = Fila()
print(fila.adicionar(10))
print(fila.adicionar(5))
print(fila.adicionar(9))
print(fila.remover())
