# 7-Classe Veiculo e polimorfismo
# Crie uma classe Veiculo com um método mover(). 
# Depois, crie subclasses Carro, Bicicleta e Aviao, cada uma com sua própria implementação de mover().

class Veiculo:
    def mover(self):
        return 'veiculo se moveu.'

class Carro(Veiculo):
    def mover(self):
        return "se move em até 200 km/h"

class Bicicleta(Veiculo):
    def mover(self):
        return "se move em até 30 km/h"

class Aviao(Veiculo):
    def mover(self):
        return 'se move em até 1000 km/h'
    
veiculos = [Carro(), Bicicleta(), Aviao()]
for veiculo in veiculos:
    print(veiculo.mover())
        