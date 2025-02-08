# 2-Classe ContaBancaria com encapsulamento
# Implemente uma classe ContaBancaria com atributos privados _saldo e _titular. 
# Adicione métodos para depositar(valor), sacar(valor) e obter_saldo().

class ContaBancaria:
    def __init__(self, saldo,titular):
        self._saldo = saldo
        self._titular = titular

    @property
    def saldo(self):
        """Getter para acessar o saldo."""
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        """Setter para modificar o saldo, garantindo que ele nunca fique negativo."""
        if valor >= 0:
            self._saldo = valor
        else:
            print('O saldo não pode ser negativo.')
    @property
    def titular(self):
        """Getter para acessar o titular."""
        return self._titular    
    
    def depositar(self):
        try:
            valor = float(input('Informe o valor a ser depositado.'))
            if valor > 0:
                self.saldo += valor
                print(f'Valor de {valor} depositado com sucesso.')
            else:
                print('Valor invalido.')
        except ValueError:
            print('Erro: Digite um número valido.')
    
    def sacar(self):
        try:
            valor = float(input('informe o valor que deseja sacar.'))
            if self.saldo > valor:
                self.saldo -= valor
                print(f'Saque de {valor} realizado com sucesso.')
            else:
                print('Saldo insuficiente para fazer esse saque.')
        except ValueError:
            print('Erro: Digite um número valido.')
        
    def obter_saldo (self):
        return f'O saldo do {self.titular} é {self.saldo}'


conta = ContaBancaria(1000,'joao')  
print(conta.saldo, conta.titular)
conta.saldo = 3000
print(conta.saldo)








