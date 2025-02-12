import pandas as pd
from pathlib import Path

class Leitura:
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self.extensao = Path(arquivo).suffix.lower()  # Obtém a extensão
        self.df = None
    
    def verificar_tipo(self):
        if self.extensao == '.csv':
            return 'csv'
        elif self.extensao == '.txt':
            return 'txt'
        else:
            return None

    def ler_arquivo(self):
        if self.verificar_tipo() == 'csv':
            self.df = pd.read_csv(self.arquivo)
        elif self.verificar_tipo() == 'txt':
            self.df = pd.read_csv(self.arquivo, sep=",")
        else:
            return 'nenhum arquivo encontrado.'
        return self.df.head()
    
    def transformar_arquivo(self):
        self.df['media'] = self.df['valor'].mean()

    def exibir_arquivos(self):
        if self.df is not None:
            return self.df.head()
        else:
            return 'nao leu nada'

leitura = Leitura('dados.csv')
print(leitura.verificar_tipo())
print(leitura.ler_arquivo())
leitura.transformar_arquivo()
print(leitura.exibir_arquivos())