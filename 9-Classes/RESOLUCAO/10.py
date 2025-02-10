# 10-Classe Funcionario com classe interna
# Crie uma classe Funcionario com um atributo endereco que é uma instância de uma classe Endereco. 
# O Endereco deve conter rua, cidade e CEP.

class Funcionario:
    class Endereco:
        def __init__(self,rua,cidade,cep):
            self.rua = rua
            self.cidade = cidade
            self.cep = cep

        def __str__(self):
            return f'Cep: {self.cep}, Cidade: {self.cidade}, Rua: {self.rua}'
    
    def __init__(self,nome,cargo,rua,cidade,cep):
        self.nome = nome
        self.cargo = cargo
        self.endereco = self.Endereco(rua,cidade,cep)
    
    def exibir_dados(self):
        return f"Nome: {self.nome}\nCargo: {self.cargo}\nEndereço: {self.endereco}"

funcionario = Funcionario('joao', 'service desk', 'florianopolis', 'capim verde', 5464556)
print(funcionario.exibir_dados())

        
    