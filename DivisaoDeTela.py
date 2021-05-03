# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carregamento da base de dados
base = pd.read_csv('trees.csv')
base.head()
# girth com volume
plt.scatter(base.Girth, base.Volume)
# girth com heigth
plt.scatter(base.Girth, base.Height)
# heigth com volume
plt.scatter(base.Height, base.Volume, marker = '*')
# hsitograma volume
plt.hist(base.Volume
         
#imprimindo juntos
# Criação de figura, no qual os gráficos serão posicionados
plt.figure(1)
plt.subplot(2,2,1)
plt.scatter(base.Girth, base.Volume)
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume, marker = '*')
plt.subplot(2,2,4)
plt.hist(base.Volume)
