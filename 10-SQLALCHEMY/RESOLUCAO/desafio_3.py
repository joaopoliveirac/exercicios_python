# Crie duas tabelas: Funcionario (com id, nome, salario) e Departamento (com id, nome, funcionario_id). 
# Faça uma consulta que traga todos os departamentos com o salário médio superior a 5000, utilizando uma subconsulta.

from sqlalchemy import Column, Integer, String, Float, ForeignKey, func
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import aliased
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    salario = Column(Float)

class Departamento(Base):
    __tablename__ = 'departamentos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    funcionario_id = Column(Integer, ForeignKey('funcionarios.id'))
    
    funcionario = relationship("Funcionario")

# Configuração do banco
db = ConexaoBD("postgres", "1234", "localhost", "5432", "desafio_3")
Base.metadata.create_all(db.engine)

sessao = db.conectar()

# Inserindo dados de exemplo
funcionarios = [
    Funcionario(nome='Carlos', salario=6000),
    Funcionario(nome='Maria', salario=5500),
    Funcionario(nome='Ana', salario=4000),
    Funcionario(nome='João', salario=7000),
    Funcionario(nome='Paula', salario=4500),
]

departamentos = [
    Departamento(nome='TI', funcionario_id=1),
    Departamento(nome='TI', funcionario_id=2),
    Departamento(nome='RH', funcionario_id=3),
    Departamento(nome='Financeiro', funcionario_id=4),
    Departamento(nome='Financeiro', funcionario_id=5),
]

sessao.add_all(funcionarios)
sessao.add_all(departamentos)
sessao.commit()

# Subconsulta para encontrar o departamento com salário médio superior a 5000
subconsulta = (
    sessao.query(Departamento.nome)
    .join(Funcionario)
    .group_by(Departamento.nome)
    .having(func.avg(Funcionario.salario) > 5000)
    .subquery()
)

# Consulta final utilizando a subconsulta
departamentos_com_salario_alto = (
    sessao.query(Departamento)
    .join(subconsulta, Departamento.nome == subconsulta.c.nome)
    .all()
)

# Exibindo os resultados
print("Departamentos com salário médio superior a 5000:")
for departamento in departamentos_com_salario_alto:
    print(f"Departamento: {departamento.nome}")
