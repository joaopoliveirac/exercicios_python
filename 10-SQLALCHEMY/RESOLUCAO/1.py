# 1. Criando uma Tabela e Inserindo Dados
# Crie uma classe Pessoa com os campos id, nome e idade. Crie a tabela no banco de dados e insira alguns registros de pessoas.
# Objetivo: Criar uma tabela e inserir dados no banco usando SQLAlchemy.
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from conexao_postgre import ConexaoBD

# Criar a base para os modelos
Base = declarative_base()

# Definir a classe Pessoa como um modelo para a tabela
class Pessoa(Base):
    __tablename__ = 'pessoas'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(30), nullable=False)
    idade = Column(Integer, nullable=False)
    cidade = Column(String(25), nullable=False)

# Função para criar a tabela e inserir dados
def criar_inserir_pessoas():
    # Criar a conexão com o banco de dados
    db = ConexaoBD("postgres", "1234", "localhost", "5432", "exercicio_1")
    
    # Criar as tabelas no banco (se ainda não existirem)
    Base.metadata.create_all(db.engine)  # Cria a tabela 'pessoas'

    # Criar uma sessão
    session = db.conectar()

    # Inserir dados na tabela
    if session:
        try:
            pessoa1 = Pessoa(nome="João", idade=30, cidade="São Paulo")
            pessoa2 = Pessoa(nome="Maria", idade=25, cidade="Rio de Janeiro")
            pessoa3 = Pessoa(nome="Carlos", idade=35, cidade="Belo Horizonte")

            # Adicionar as pessoas à sessão
            session.add(pessoa1)
            session.add(pessoa2)
            session.add(pessoa3)

            # Commit para salvar no banco de dados
            session.commit()
            print("Pessoas inseridas com sucesso!")
        
        except Exception as e:
            session.rollback()  # Rollback em caso de erro
            print(f"Erro ao inserir dados: {e}")
        
        finally:
            # Fechar a sessão
            db.fechar_conexao(session)

# Chamar a função para criar e inserir dados
criar_inserir_pessoas()




