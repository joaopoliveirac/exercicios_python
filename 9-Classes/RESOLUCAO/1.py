# 1-Classe Pessoa e herança
# Crie uma classe Pessoa com atributos nome e idade. 
# Depois, crie uma subclasse Funcionario que adiciona cargo e salario. Implemente um método aumentar_salario(porcentagem).

class Pessoa:
    tipo = 'humano'
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def exibir_dados(self):
        return f"{self.nome} tem {self.idade}"

class Funcionario(Pessoa):
    def __init__(self, nome, idade,cargo,salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario
    
    def aumentar_salario(self,porcentagem):
        aumento = self.salario * (porcentagem / 100)
        self.salario += aumento
        return f'Novo salario do {self.nome} é de {self.salario}'
    
    def exibir_dados(self):
        return f'{super().exibir_dados()}, cargo: {self.cargo} e salario: {self.salario}'
    
func = Funcionario('Joao', 25, 'service desk', 2000)
print(func.exibir_dados())
print(func.aumentar_salario(10))

#apanhei mais que tudo pra entender essa parte de classe, primeira vez que vi foi no bootcamp do Luciano,
#porem fiquei meio perdido... depois de mais de 3 horas conseguir resolver esse exercicio
        