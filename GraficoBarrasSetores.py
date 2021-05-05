# Importação do pandas para leitura de arquivos .csv
import pandas as pd

# Carregamento da base de dados
base = pd.read_csv('insect.csv')
base.shape
#dados
base.head()
# Agrupamento dos dados baseado no atributo 'spray', contando e somando os registros
agrupado = base.groupby(['spray'])['count'].sum()
agrupado
# Gráfico de barras
agrupado.plot.bar(color = 'gray')
#cores
agrupado.plot.bar(color = ['blue','yellow','red','green','pink','orange'])
# Gráfico de pizza
agrupado.plot.pie()
#com legenda
agrupado.plot.pie(legend = True)
