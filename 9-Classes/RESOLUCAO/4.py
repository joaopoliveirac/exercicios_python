# 4-Classe Produto com desconto
# Implemente uma classe Produto com nome, preco e um método aplicar_desconto(porcentagem). 
# O preço deve ser atualizado corretamente.

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = float(preco)
        
    
    def aplicar_desconto(self,porcentagem):
        self.preco_novo = self.preco * (1- porcentagem / 100)
        return f'{self.nome} era {self.preco}, ganhou {porcentagem} % de desconto e saiu por {self.preco_novo}'

p1 = Produto('computador', 2000)
print(p1.aplicar_desconto(20))

