# 9. Consultas com Ordenação e Limite
# Crie uma classe Produto com os campos id, nome e preco. 
# Insira vários produtos e, depois, faça uma consulta que ordene os produtos pelo preço de forma decrescente e limite o resultado a 5 produtos.

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    preco = Column(Float)

db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_9")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

# Inserindo vários produtos
produtos = [
    Produto(nome='Celular', preco=2500),
    Produto(nome='Notebook', preco=5000),
    Produto(nome='Monitor', preco=1200),
    Produto(nome='Mouse', preco=150),
    Produto(nome='Teclado', preco=300),
    Produto(nome='Headset', preco=450),
    Produto(nome='Impressora', preco=1100),
    Produto(nome='Cadeira Gamer', preco=750),
    Produto(nome='Mesa Escritório', preco=950),
    Produto(nome='Placa de Vídeo', preco=4000)
]

sessao.add_all(produtos)
sessao.commit()

# Consulta com ordenação decrescente pelo preço e limite de 5 produtos
consulta = sessao.query(Produto).order_by(Produto.preco.desc()).limit(5).all()

print("Top 5 produtos mais caros:")
for produto in consulta:
    print(f"Nome: {produto.nome}, Preço: R${produto.preco}")












