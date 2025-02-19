# 6. Relacionamento Muitos-para-Muitos
# Crie uma classe Aluno e uma classe Curso. 
# Um aluno pode estar matriculado em vários cursos e um curso pode ter vários alunos. 
# Crie o relacionamento muitos-para-muitos entre as tabelas.

from sqlalchemy import Column, String, Integer, ForeignKey, Table
from sqlalchemy.orm import declarative_base,relationship
from conexao_postgre import ConexaoBD

Base = declarative_base()

#tabela intermediaria
aluno_curso = Table('aluno_curso', Base.metadata,
                    Column('aluno_id', Integer, ForeignKey('alunos.id')),
                    Column('curso_id', Integer, ForeignKey('cursos.id')))

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key = True)
    nome = Column(String(40))

    cursos = relationship('Curso', secondary = aluno_curso, back_populates = 'alunos')


class Curso(Base):
    __tablename__ = 'cursos'
    id = Column(Integer, primary_key = True)
    nome = Column(String(40))

    alunos = relationship('Aluno', secondary = aluno_curso, back_populates = 'cursos')

db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_6")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

alunos = [Aluno(nome = 'joao'),
          Aluno(nome = 'Maria'),
          Aluno(nome = 'ricardo')]

sessao.add_all(alunos)
sessao.commit()

cursos = [Curso(nome = 'matematica'),
          Curso(nome = 'quimica'),
          Curso(nome = 'fisica')]

sessao.add_all(cursos)
sessao.commit()

#associando alunos aos cursos
aluno_1 = sessao.query(Aluno).filter(Aluno.nome == 'joao').first()
aluno_2 = sessao.query(Aluno).filter(Aluno.nome == 'Maria').first()
aluno_3 = sessao.query(Aluno).filter(Aluno.nome == 'ricardo').first()
curso_1 = sessao.query(Curso).filter(Curso.nome == 'matematica').first()
curso_2 = sessao.query(Curso).filter(Curso.nome == 'quimica').first()
curso_3 = sessao.query(Curso).filter(Curso.nome == 'fisica').first()

aluno_1.cursos = [curso_1,curso_2,curso_3]
aluno_2.cursos = [curso_2,curso_3]
aluno_3.cursos =[curso_3]

sessao.commit()