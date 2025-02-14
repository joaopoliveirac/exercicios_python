# 1. Criando uma Tabela e Inserindo Dados
# Crie uma classe Pessoa com os campos id, nome e idade. Crie a tabela no banco de dados e insira alguns registros de pessoas.
# Objetivo: Criar uma tabela e inserir dados no banco usando SQLAlchemy.

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class 