# 5. Relacionamento Um-para-Muitos
# Crie duas classes: Autor e Livro. Um autor pode ter vários livros. Insira um autor e vários livros relacionados a ele.

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30))

    # Relacionamento com livros
    livros = relationship("Livro", back_populates="autor")

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    nome_livro = Column(String(30))
    autor_id = Column(Integer, ForeignKey('autores.id'))
    
    # Relacionamento com autor
    autor = relationship("Autor", back_populates="livros")

# Criando conexão com o banco de dados
db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_5")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

# Inserindo autores
autores = [Autor(nome='josefino'),
           Autor(nome='Pedroalvarescabral'),
           Autor(nome='josedasilva')]

sessao.add_all(autores)
sessao.commit()

# Inserindo livros e associando-os diretamente aos autores utilizando o ID
livros = [
    Livro(nome_livro='agua santa das claras', autor_id=sessao.query(Autor).filter(Autor.nome == 'Pedroalvarescabral').first().id),
    Livro(nome_livro='cheira flors', autor_id=sessao.query(Autor).filter(Autor.nome == 'josefino').first().id),
    Livro(nome_livro='dragao dos zodiacos', autor_id=sessao.query(Autor).filter(Autor.nome == 'josefino').first().id),
    Livro(nome_livro='testeilvro', autor_id=sessao.query(Autor).filter(Autor.nome == 'josedasilva').first().id),
    Livro(nome_livro='aagua de santo', autor_id=sessao.query(Autor).filter(Autor.nome == 'josedasilva').first().id),
    Livro(nome_livro='agutestemercado', autor_id=sessao.query(Autor).filter(Autor.nome == 'josedasilva').first().id),
    Livro(nome_livro='aalaoalo', autor_id=sessao.query(Autor).filter(Autor.nome == 'josedasilva').first().id)
]

sessao.add_all(livros)
sessao.commit()
sessao.close()

    