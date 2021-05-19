from numpy.core.fromnumeric import shape
import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib.pyplot import axis, figure, show, bar, xlabel, ylabel, title, plot
import seaborn as sns
from six import assertCountEqual

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
sns.set() # Setando as configs padrões de exibição de gráficos da lib 'seaborn'
figure(figsize=(8, 6)) # Definindo a configuração de dimensões do gráfico plotado
ax = sns.countplot(x = 'composto', data=consulta_compostos, order=idx_compostos) # Plot ordenado de gráfico de barras das frequências de 'compostos' mais testados.
ax.set_title('5 COMPOSTOS MAIS FREQUENTES') # Definindo um título para a visualização corrente
ylabel('FREQUÊNCIA')
xlabel('COMPOSTOS')
show()