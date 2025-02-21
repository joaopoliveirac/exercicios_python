# 8. Consultas com Join
# Crie as classes Autor e Livro (como no exercício 5). 
# Faça uma consulta que traga os livros junto com o nome do autor utilizando join.
# Um autor pode ter vários livros. Insira um autor e vários livros relacionados a ele.

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40))

    livros = relationship("Livro", back_populates="autor")

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    id_autor = Column(Integer, ForeignKey('autores.id'))

    autor = relationship("Autor", back_populates="livros")

db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_8")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

# Inserindo autores
autores = [
    Autor(nome='josefino'),
    Autor(nome='Pedroalvarescabral'),
    Autor(nome='josedasilva')
]

sessao.add_all(autores)
sessao.commit()

# Pegando os IDs dos autores
autor_josefino = sessao.query(Autor).filter(Autor.nome == 'josefino').first()
autor_pedro = sessao.query(Autor).filter(Autor.nome == 'Pedroalvarescabral').first()
autor_jose = sessao.query(Autor).filter(Autor.nome == 'josedasilva').first()

# Inserindo livros
livros = [
    Livro(nome='Agua Santa das Claras', id_autor=autor_pedro.id),
    Livro(nome='Cheira Flors', id_autor=autor_josefino.id),
    Livro(nome='Dragão dos Zodíacos', id_autor=autor_josefino.id),
    Livro(nome='Teste Livro', id_autor=autor_jose.id),
    Livro(nome='A Água de Santo', id_autor=autor_jose.id),
    Livro(nome='Agua Teste Mercado', id_autor=autor_jose.id),
    Livro(nome='Alao Alo', id_autor=autor_jose.id)
]

sessao.add_all(livros)
sessao.commit()

consulta = sessao.query(Livro, Autor).join(Autor).all()

for livro, autor in consulta:
    print(f'Livro: {livro.nome}, Autor: {autor.nome}')



