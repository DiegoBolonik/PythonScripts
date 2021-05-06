# Importação das bibliotecas
from sklearn import datasets
import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Carregamento da base de dados 
iris = datasets.load_iris()
# visualização de quantos registros existem por classe
unicos, quantidade = np.unique(iris.target, return_counts = True)
unicos

quantidade

# Agrupamento com k-means, utilizando 3 clusters (de acordo com a base de dados)
cluster = KMeans(n_clusters = 3)
cluster.fit(iris.data)
# Visualização dos três centroides
centroides = cluster.cluster_centers_
centroides
# Visualização dos grupos que cada registro foi associado
previsoes = cluster.labels_
previsoes
# Contagem dos registros por classe
unicos2, quantidade2 = np.unique(previsoes, return_counts = True)
unicos2

quantidade2

# Geração da matriz de contingência para comparar os grupos com a base de dados
resultados = confusion_matrix(iris.target, previsoes)
resultados

# Geração do gráfico com os clusters gerados, considerando para um (previsoes 0, 1 ou 2)
# Usamos somente as colunas 0 e 1 da base de dados original para termos 2 dimensões
plt.scatter(iris.data[previsoes == 0, 0], iris.data[previsoes == 0, 1], 
            c = 'green', label = 'Setosa')
plt.scatter(iris.data[previsoes == 1, 0], iris.data[previsoes == 1, 1], 
            c = 'red', label = 'Versicolor')
plt.scatter(iris.data[previsoes == 2, 0], iris.data[previsoes == 2, 1], 
            c = 'blue', label = 'Virgica')
plt.legend()
