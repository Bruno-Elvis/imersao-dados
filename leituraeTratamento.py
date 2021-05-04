from numpy.core.fromnumeric import shape
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

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
print("Quantidade de registros (frequência) por classificação:\n", dados['tratamento'].value_counts(), "\nNúmero total de registros da Classe: ", dados['tratamento'].count())
print()

# NORMALIZAÇÃO #
proporcao_tratamento = dados['tratamento'].value_counts(normalize = True) * 100
proporção_dose = dados['dose'].value_counts(normalize = True) * 100

print("Proporção da classe 'tratamento':\n", proporcao_tratamento)
print()

plt.pie(proporcao_tratamento)
plt.show()
print()

print(shape(dados['droga'].unique()))
print(dados['droga'].value_counts())