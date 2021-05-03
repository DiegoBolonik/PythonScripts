# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carregamento da base de dados
base = pd.read_csv('trees.csv')
base.head()
# Geração do boxplot
# patch_artist = True preenche, showfliers outliers
plt.boxplot(base.Volume, vert = False, showfliers = False, notch = True,patch_artist = True)
plt.title('Árvores')
plt.xlabel('Volume')
#dados por linha
plt.boxplot(base)
plt.title('Árvores')
plt.xlabel('Dados')

# Geração de 3 boxplots, cada um mostrado informações diferentes
plt.boxplot(base.Volume, vert = False)
plt.boxplot(base.Girth, vert = False)
plt.boxplot(base.Height, vert = False)
plt.title('Árvores')
plt.xlabel('Dados')
