from numpy.core.fromnumeric import shape
import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib.pyplot import show, bar, ylabel, xlabel, title
import seaborn as sns

url_dados_origem = 'https://github.com/Bruno-Elvis/imersaoDados/blob/master/dados/dados_experimentos.zip?raw=true'
dados_origem_local = 'E:\Arquivos\LEARNS\Python\ImersaoDados\dados\dados_experimentos.csv'

#dados = pd.read_csv(url_dados_origem, compression = 'zip')
dados = pd.read_csv(dados_origem_local)

#print(dados) #Lê os dados completos da origem de dados

print(dados.head()) #Retorna as 5 primeiras linhas incluindo o cabeçalho para visualização da cadeia de dados
print()
print(dados.tail()) #Retorna as 5 últimas linhas incluindo o cabeçalho para visualização da cadeia de dados
print()
print(shape(dados))
print()

# CONTROLE #
controle_tratamento = dados['tratamento'].unique()
controle_tempo = dados['tempo'].unique()
controle_dose = dados['dose'].unique()
controle_droga = dados['droga'].unique()

print("Controle da classe 'tratamento': ", controle_tratamento)
print("Controle da classe 'tempo': ", controle_tempo)
print("Controle da classe 'dose': ", controle_dose)
print("Controle da classe 'droga': ", controle_droga)
print("Controle da classe 'g-0': ", dados['g-0'].unique()) #Valores relacionados aos efeitos do experimento
# Coluna g-x  está normalizada (Normalmente é 'arredondado' os valores de g-x com a finalidade de remover os efeitos não esperados (não-biológicos))
print()

# FREQÊNCIA #
print(" --- FREQUÊNCIA --- ")
print("Quantidade de registros (frequência) por classificação:\n", dados['tratamento'].value_counts(), "\nNúmero total de registros da Classe: ", dados['tratamento'].count())
print()

# NORMALIZAÇÃO #
print(" --- NORMALIZAÇÃO --- ")
proporcao_tratamento = dados['tratamento'].value_counts(normalize = True) * 100
proporcao_dose = dados['dose'].value_counts(normalize = True) * 100
proporcao_tempo = dados['tempo'].value_counts(normalize = True) * 100

print("Proporção da classe 'tempo':\n", proporcao_tempo, type(proporcao_tempo))
print("Proporção ('tempo'):\n", proporcao_tempo.values)
print("Controle ('tempo'):\n", controle_tempo)
print()
print("Apresentar apenas os valores dos índices da consulta no DataFrame:\n", dados['droga'].value_counts().index[:5])
print()

print("--- CONTADORES --- ")
print("Quantidade de Drogas via método 'shape': ", shape(dados['droga'].unique()))
print()
print("Quantidade de Drogas via método 'len': ", len(dados['droga'].unique()))
print()
print("Quantidade de Drogas via método 'nunique': ", dados['droga'].nunique())
print()

print(" --- FILTRAGEM --- ")
print(dados[dados['g-0'] > 0].head()) # Definição de 'Máscara' nos dados de origem, onde 'g-0' é maior que 0 (5 primeiros)
#QUERY
print()

print(" --- PLOTAGEM DE GRAFICOS --- ")
### GRÁFICO DE BARRAS (matplotlib.pyplot) ###

# GRÁFICO DE CONTROLE (TRATAMENTOS) #
'''
tratamento_index = dados['tratamento'].value_counts().index
tratamento_val = proporcao_tratamento.values

ylabel('FREQUÊNCIA')
xlabel('TRATAMENTOS')
title('CONTROLE-TRATAMENTOS')

bar(tratamento_index, tratamento_val)
show()
'''

# GRÁFICO DE CONTROLE (DOSES) #
'''
dose_index = dados['dose'].value_counts().index
dose_val = proporcao_dose.values

ylabel('FREQUÊNCIA')
xlabel('DOSES')
title('CONTROLE-DOSES')

bar(dose_index, dose_val)
show()
'''

# GRÁFICO DE CONTROLE (TEMPO) #
'''
tempo_index = dados['tempo'].value_counts().index
tempo_val = proporcao_tempo.values

ylabel('FREQUÊNCIA')
xlabel('TEMPO')
title('CONTORLE-TEMPO')

bar(tempo_index, tempo_val)
show()
'''

### GRÁFICO DE BARRAS (seaborn) ###
sns.countplot(x = 'droga', data=dados)

sns.countplot(data=dados,  x=dados['droga'], y='FREQUÊNCIA')
show()

# tentando renomear colunas
# colunas_dados = np.array(dados.columns)
# print("Colunas: ", colunas_dados)
# print(dados.rename(columns={'g-0' : 'g0'}).head()) #renomeando a coluna 'g-0' para 'g0'
# Utilizar o parâmetro inplace=true' para definir e atribuir as alterações no DataFrame de origem (dados)
# df.rename({'a': 'X', 'b': 'Y'}, inplace=True)
print()
# renomear as conulas de genes removendo o 'hífen' pois pode gerar erros no interpretador python