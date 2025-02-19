# 3. Atualizando Registros
# Crie uma classe Cliente com os campos id, nome e email. 
# Insira um cliente e, em seguida, atualize o email de um cliente específico.

from sqlalchemy import Integer, String,Column
from sqlalchemy.orm import declarative_base
from conexao_postgre import ConexaoBD

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key = True)
    nome = Column(String(30))
    email = Column(String(20))

db = ConexaoBD('postgres', '1234', 'localhost', '5432', 'exercicio_3')
Base.metadata.create_all(db.engine)
sessao = db.conectar()

clientes = [Cliente(nome = 'joao', email = 'joaopo@gmail.com'),
             Cliente(nome = 'pedro henrique', email = 'pedro@gmail.com')]

sessao.add_all(clientes)
sessao.commit()

update = sessao.query(Cliente).filter(Cliente.nome == 'joao').update( {'nome': 'zezedicarmargo'}, synchronize_session=False)

consulta = sessao.query(Cliente).all()
for cliente in consulta:
    print(cliente.id, cliente.nome, cliente.email)





