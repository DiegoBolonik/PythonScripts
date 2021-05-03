# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregamento da base de dados
base = pd.read_csv('trees.csv')
base.head()
# Gráfico de dispersão considerando o volume e a dispersão
plt.scatter(base.Girth, base.Volume, color = 'blue', facecolors = 'none', marker = '*')
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferência')
# Gráfico de linha considerando o volume e o atributo "girth"
plt.plot(base.Girth, base.Volume)
plt.title('Árvores')
plt.xlabel('Volume')
plt.ylabel('Circunferência')
# Gráfico de dispersão com 'afastamento' dos dados (jitter)
#fit_reg linha de tendência
sns.regplot(base.Girth, base.Volume, data = base, x_jitter = 0.3, fit_reg = False)
