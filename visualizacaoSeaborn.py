from numpy.core.fromnumeric import shape
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

url_dados_origem = 'https://github.com/Bruno-Elvis/imersaoDados/blob/master/dados/dados_experimentos.zip?raw=true'
dados_origem_local = 'E:\Arquivos\LEARNS\Python\ImersaoDados\dados\dados_experimentos.csv'

dados = pd.read_csv(dados_origem_local)

# Renomeando Colunas #
# colunas_dados = np.array(dados.columns)
# print("Colunas: ", colunas_dados)
mapaColunas = {'droga' : 'composto'}
dados.rename(columns=mapaColunas, inplace=True)
# o parâmetro inplace=true' para definir e atribuir as alterações no DataFrame de origem (dados)

print(dados.rename(columns={'g-0' : 'g0'}).head()) #renomeando a coluna 'g-0' para 'g0' e exibindo as 5 primeiras tuplas do dataframe
print()
# renomear as conulas de genes removendo o 'hífen' pois pode gerar erros no interpretador python

idx_compostos = dados['composto'].value_counts().index[:5]
print("Print", idx_compostos)

consulta_compostos = dados.query('composto in @idx_compostos')

### GRÁFICO DE BARRAS COM A LIB (seabor) ###
sns.set() # Setando as configs padrões de exibição de gráficos da lib 'seaborn'.
plt.figure(figsize = (8, 6)) # Definindo a configuração de dimensões do gráfico plotado.

ax = sns.countplot(x = 'composto', data = consulta_compostos, order = idx_compostos) # Plot ordenado de gráfico de barras das frequências de 'compostos' mais testados.

# CONFIGURANDO AS LABELS DO GRÁFICO (seaborn) #
'''
formatFonte = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 15} # Define a formatação global da fonte nas visualizações.

ax.set_title('5 COMPOSTOS MAIS FREQUENTES', formatFonte) # Definindo um título para a visualização corrente
ax.set_ylabel('FREQUÊNCIA', formatFonte)
ax.set_xlabel('COMPOSTOS', formatFonte)
'''
# OR (Label Individualmente) #
ax.set_title('5 COMPOSTOS MAIS FREQUENTES', size = 14, family = '', weight = 'bold') # Definindo um título para a visualização corrente.
ax.set_ylabel('FREQUÊNCIA', size = 12)
ax.set_xlabel('COMPOSTOS', size = 12)
# OR #
# CONFIGURANDO AS LABELS DO GRÁFICO (matplotlib/pyplot) #
'''
plt.ylabel('FREQUÊNCIA')
plt.xlabel('COMPOSTOS')
plt.title('5 COMPOSTOS MAIS FREQUENTES')
'''
plt.show()
print()

#VERIFICANDO AS DIMENÇÕES DE CADA COMPOSTO

tam_g0 = dados['g-0'].nunique()
print("Quantidade de resultados do composto 'g-0': ", tam_g0)
print()

result_max_g0 = dados['g-0'].max()
result_min_g0 = dados['g-0'].min()
print("Valor mínimo em g0 = {}, valor máximo = {}".format(result_min_g0, result_max_g0))
print()

# PLOTANDO HISTOGRAMA DA 'g-0' #

dados['g-0'].hist(bins = 100)
plt.ylabel('FREQUÊNCIA')
plt.xlabel('RESULTADOS')
plt.title("HISTOGRAMA DOS RESULTADOS NA 'G-0'", weight = 'bold')
plt.subplot(2, 1, 1)
#Me apresentou através do grafico apresentado ser uma 'curva normal' dos resultados #

dados['g-5'].hist(bins = 100)
plt.ylabel('FREQUÊNCIA')
plt.xlabel('RESULTADOS')
plt.title("HISTOGRAMA DOS RESULTADOS NA 'G-5'", weight = 'bold')
plt.subplot(2, 1, 2)

plt.show()