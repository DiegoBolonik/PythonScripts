# Importação das bibliotecas: pandas para carregar arquivos .csv e numpy para gerar números aleatórios
import pandas as pd
import numpy as np

# Carregamento da base de dados (o arquivo .csv precisa estar na mesma pasta do código fonte) e visualização dos dados
base = pd.read_csv('iris.csv')
base
# Verificar quantas linhas e colunas existem na base de dados, 150 linhas e 5 colunas
base.shape
# Mudança da semente aleatória randômica para manter os resultados em várias execuções
np.random.seed(2345)
# 150 amostras, de 0 a 1, com reposição, probabilidades equivalentes
amostra = np.random.choice(a = [0, 1], size = 150, replace = True,
                           p = [0.7, 0.3])
# Verificar tamanho da amostra
#len(amostra)
# Verificar tamanho da amostra para valores igual a 1 e 0
#len(amostra[amostra == 1])
#len(amostra[amostra == 0])
amostra
base_final = base.loc[amostra == 0]
base_final.shape
base_final2 = base.loc[amostra == 1]
base_final2.shape
