# Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Carregamento da base de dados
base = pd.read_csv('trees.csv')
base.shape
#dados
base.head()
# Criação do histograma, considerando somente o segundo atributo da base de dados e com duas divisões (bins)
# A variável 'h' armazena as faixas de valores de Height
h = np.histogram(base.iloc[:,1], bins = 6)
h
# Visualização do histograma com 6 divisões (bins)
plt.hist(base.iloc[:,1], bins = 6)
plt.title('Árvores')
plt.ylabel('Frequência')
plt.xlabel('Altura')
