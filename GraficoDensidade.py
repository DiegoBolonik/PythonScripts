# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento da base de dados
base = pd.read_csv('trees.csv')
base.head()
# Histograma com 10 divisões (bins) e somente para o primeiro atributo da base de dados
plt.hist(base.iloc[:,1], bins = 6)
# Histograma com a linha de distribuição de frequência, com 6 divisões (bins)
#kde = linha de densidade
sns.distplot(base.iloc[:,1], hist = True, kde = False,
             bins = 6, color = 'blue',
             hist_kws={'edgecolor': 'black'})
#densidade
sns.distplot(base.iloc[:,1], hist = False, kde = True,
             bins = 6, color = 'blue',
             hist_kws={'edgecolor': 'black'})
#densidade e histograma
sns.distplot(base.iloc[:,1], hist = True, kde = True,
             bins = 6, color = 'blue',
             hist_kws={'edgecolor': 'black'})
