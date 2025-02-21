# 7. Criando um Índice
# Crie uma tabela Produto com os campos id, nome, descricao e preco. Crie um índice para o campo preco.

from sqlalchemy import Column, Integer, String, Float, Index
from sqlalchemy.orm import declarative_base
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key = True)
    nome = Column(String(30))
    descricao = Column(String(50))
    preco = Column(Float, index = True)

db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_7")

Base.metadata.create_all(db.engine)

sessao = db.conectar()

produtos = [Produto(nome = 'arroz', descricao = 'arroz piracanjuba', preco = 35),
            Produto(nome = 'feijao', descricao = 'feijao carioca', preco = 15),
            Produto(nome = 'oleo', descricao = 'oleo de soja', preco = 25),
            Produto(nome = 'cafe', descricao = 'cafe extra forte', preco = 40),
            Produto(nome = 'coxao mole', descricao = 'carne de primeira', preco = 50),]

sessao.add_all(produtos)
sessao.commit()





