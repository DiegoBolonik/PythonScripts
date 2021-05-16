# Importação das bibliotecas
import numpy as np
import pandas as pd
from math import ceil

# Criação das variáveis para representar a população, a amostra e o valor de k
populacao = 150
amostra = 15
k = ceil(populacao / amostra)
print(k)
# Definição do valor randômico para inicializar a amostra, iniciando em 1 até k + 1
r = np.random.randint(low = 1, high = k + 1, size = 1)
print(r)

# Criamos um for para somar os próximos valores, baseado no primeiro valor r que foi definido acima
acumulador = r[0]
sorteados = []
for i in range(amostra):
    #print(acumulador)
    sorteados.append(acumulador)
    acumulador += k
print(sorteados)
len(sorteados)

# Carregamos a base de dados e criamos a base_final somente com os valores sorteados
base = pd.read_csv('iris.csv')
dataset = pd.read_csv('iris.csv', sep=';', index_col=0)

base_final = base.loc[sorteados]
base_final
