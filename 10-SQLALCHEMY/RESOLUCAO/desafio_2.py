# Crie uma tabela Venda com os campos id, produto, quantidade e preco_unitario. 
# Calcule o valor total de vendas de cada produto e mostre a soma total de vendas de todos os produtos.

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy import func
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True)
    produto = Column(String(50))
    quantidade = Column(Integer)
    preco_unitario = Column(Float)

    @property
    def valor_total(self):
        return self.quantidade * self.preco_unitario

# Configuração do banco
db = ConexaoBD("postgres", "1234", "localhost", "5432", "desafio_2")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

# Inserindo vendas
vendas = [
    Venda(produto='Produto A', quantidade=10, preco_unitario=20.0),
    Venda(produto='Produto B', quantidade=5, preco_unitario=50.0),
    Venda(produto='Produto C', quantidade=8, preco_unitario=15.0),
    Venda(produto='Produto A', quantidade=3, preco_unitario=20.0),
    Venda(produto='Produto B', quantidade=7, preco_unitario=50.0),
]

sessao.add_all(vendas)
sessao.commit()

# Consulta para calcular o valor total de cada venda e a soma total de vendas
vendas_produto = sessao.query(Venda.produto, func.sum(Venda.quantidade * Venda.preco_unitario).label("total_vendas")) \
                       .group_by(Venda.produto) \
                       .all()

print("Valor total de vendas por produto:")
for venda in vendas_produto:
    print(f"Produto: {venda.produto}, Total Vendas: R${venda.total_vendas:.2f}")

# Soma total de todas as vendas
soma_total_vendas = sessao.query(func.sum(Venda.quantidade * Venda.preco_unitario)).scalar()

print(f"\nSoma total de vendas de todos os produtos: R${soma_total_vendas:.2f}")
