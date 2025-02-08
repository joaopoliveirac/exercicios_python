# 3-Classe Carro com contagem de instâncias
# Crie uma classe Carro com os atributos marca, modelo e ano. 
# Adicione um atributo de classe quantidade_carros que aumenta sempre que um novo carro é instanciado.

# Instância é o ato de criar a "ocorrência",
# Objeto é a "coisa real" resultante dessa criação.

class Carro:
    contador = 0

    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Carro.contador += 1
    
    def exibir_carro(self):
        return f'O carro é da {self.marca}, modelo {self.modelo} e de {self.ano}. Já foram criados {Carro.contador}'

carro = Carro('Toyota', 'onix', '2010')
carro_1 = Carro('Volks', 'gol', '2015')
print(carro.exibir_carro())
print(carro.exibir_carro())
