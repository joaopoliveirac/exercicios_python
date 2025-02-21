# 1. Trabalhando com Transactions
# Crie um sistema simples com duas tabelas: ContaBancaria e Transacao. 
# Realize uma transação para transferir um valor entre duas contas, 
# garantindo que ambas as operações de débito e crédito sejam executadas dentro de uma única transação.

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from conexao_postgre import ConexaoBD

Base = declarative_base()

class ContaBancaria(Base):
    __tablename__ = 'contas_bancarias'
    id = Column(Integer, primary_key=True)
    numero_conta = Column(String(20), unique=True)
    saldo = Column(Float, default=0.0)
    
    # Relacionamento com a tabela Transacao
    transacoes = relationship("Transacao", back_populates="conta")

class Transacao(Base):
    __tablename__ = 'transacoes'
    id = Column(Integer, primary_key=True)
    valor = Column(Float)
    data = Column(String, default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    tipo = Column(String)  # 'debito' ou 'credito'
    id_conta = Column(Integer, ForeignKey('contas_bancarias.id'))
    
    conta = relationship("ContaBancaria", back_populates="transacoes")

# Função que realiza a transferência
def transferir(sessao, conta_origem_id, conta_destino_id, valor):
    try:
        # Iniciando a transação
        conta_origem = sessao.query(ContaBancaria).get(conta_origem_id)
        conta_destino = sessao.query(ContaBancaria).get(conta_destino_id)
        
        if conta_origem and conta_destino and conta_origem.saldo >= valor:
            # Débito da conta de origem
            conta_origem.saldo -= valor
            transacao_origem = Transacao(valor=valor, tipo="debito", conta=conta_origem)
            
            # Crédito na conta de destino
            conta_destino.saldo += valor
            transacao_destino = Transacao(valor=valor, tipo="credito", conta=conta_destino)
            
            # Adicionando transações
            sessao.add(transacao_origem)
            sessao.add(transacao_destino)
            
            # Commit da transação
            sessao.commit()
            print(f"Transferência de R${valor} realizada com sucesso!")
        else:
            print("Transferência não realizada. Verifique os saldos ou contas.")
            sessao.rollback()  # Caso algo dê errado, reverte a transação
    except SQLAlchemyError as e:
        print(f"Erro durante a transação: {e}")
        sessao.rollback()

# Configuração do banco e inserção de contas
db = ConexaoBD("postgres", "1234", "localhost", "5432", "desafio_1")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

# Criando algumas contas bancárias para teste
conta1 = ContaBancaria(numero_conta="12345", saldo=5000.0)
conta2 = ContaBancaria(numero_conta="67890", saldo=2000.0)

sessao.add_all([conta1, conta2])
sessao.commit()

# Realizando uma transferência entre as contas
transferir(sessao, conta_origem_id=conta1.id, conta_destino_id=conta2.id, valor=1000.0)

# Verificando os saldos após a transferência
conta_origem = sessao.query(ContaBancaria).get(conta1.id)
conta_destino = sessao.query(ContaBancaria).get(conta2.id)

print(f"Saldo da conta {conta1.numero_conta}: R${conta_origem.saldo}")
print(f"Saldo da conta {conta2.numero_conta}: R${conta_destino.saldo}")
