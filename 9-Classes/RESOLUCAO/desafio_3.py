# 3-Classe DataFramePersonalizado usando Pandas
# Crie uma classe DataFramePersonalizado que encapsula um pandas.DataFrame, 
# adicionando métodos como filtrar(coluna, valor), ordenar(coluna), e agrupar(coluna, funcao).
import pandas as pd

class DataFramePersonalizado:
    def __init__(self,arquivo):
        self.arquivo = arquivo
        self._df = None
    
    def ler_arquivo(self):
        self._df = pd.read_csv(self.arquivo)
        if self._df is not None:
            return 'arquivo lido com sucesso.'
        else:
            return 'nenhum arquivo carregado.'
    
    def filtrar_por_coluna(self,coluna,valor):
        return self._df[self._df[coluna] == valor]
    
    def ordenar(self,coluna):
        return self._df.sort_values(by=coluna, ascending=True)
    
    def agrupar(self,coluna):
        return self._df.groupby(coluna, as_index=False).sum(numeric_only=True)
    
dataframe = DataFramePersonalizado('dados.csv')
print(dataframe.ler_arquivo())
print(dataframe.filtrar_por_coluna('nome','joao'))
print(dataframe.ordenar('idade'))
print(dataframe.agrupar('sexo'))

