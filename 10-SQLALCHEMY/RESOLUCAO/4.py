# 4. Deletando Registros
# Crie uma classe Funcionario com os campos id, nome e salario. 
# Insira alguns funcionários e, depois, exclua um funcionário pelo seu ID.

from sqlalchemy import Column, Integer, String,Float
from sqlalchemy.orm import declarative_base
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key = True)
    nome = Column(String(30))
    salario = Column(Float)

db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_4")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

funcionarios = [Funcionario(nome = 'joao', salario = 5000),
                Funcionario(nome = 'pedro', salario = 3000),
                Funcionario(nome = 'zeze', salario = 4000)]

sessao.add_all(funcionarios)
sessao.commit()

sessao.query(Funcionario).filter(Funcionario.nome == 'joao').delete()
sessao.commit()

consulta = sessao.query(Funcionario).filter(Funcionario.nome == 'joao').all()

for funcionario in consulta:
    print(funcionario.id,funcionario.nome, funcionario.salario)

