# 1-Classe ETL com transformação de dados
# Crie uma classe ETL com os métodos extrair(), transformar() e carregar(). 
# O método extrair() deve ler um arquivo CSV, transformar() deve converter os valores para um formato específico, 
# e carregar() deve salvar os dados em um novo arquivo
import pandas as pd

class ETL:
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.df = None
    
    def extrair(self):
        self.df = pd.read_csv(self.arquivo)
        return self.df
    
    def transformar(self,coluna):
        if self.df is not None:
            self.df[coluna] = pd.to_datetime(self.df[coluna], format= '%Y-%m-%d')
        else:
            print('nenhum arquivo foi extraido.')
        
    
    def carregar(self,nome_arquivo):
        return self.df.to_csv(nome_arquivo)

etl = ETL('dados_etl.csv')
etl.extrair()
etl.transformar('data_nascimento')
etl.carregar('teste_1.csv')


        

    