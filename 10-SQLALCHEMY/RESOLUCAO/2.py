# 2. Consultando Dados
# Crie a classe Produto com os campos id, nome e preco. 
# Insira pelo menos três produtos na tabela e faça uma consulta para exibir todos os produtos com preço superior a 50.

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key = True)
    nome = Column(String(30), nullable = False)
    preco = Column(Float, nullable = False)

db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_2")
Base.metadata.create_all(db.engine)

if __name__ == '__main__':
    sessao = db.conectar()

    produtos = [Produto(nome = 'arroz', preco = 5000),
                Produto(nome='feijao', preco = 70),
                Produto(nome = 'farofa', preco = 37)]
    
    sessao.add_all(produtos)
    sessao.commit()
    sessao.close()


