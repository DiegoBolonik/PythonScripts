# Importação das bibliotecas: scipy para gerar estatísticas mais detalhadas
import numpy as np
from scipy import stats

# Criação da variável com os dados dos jogadores, visualização da mediana e média
jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]
np.mean(jogadores)
np.median(jogadores)
# Criação da variável para geração dos quartis (0%, 25%, 50%, 75% e 100%) 
quartis = np.quantile(jogadores, [0, 0.25, 0.5, 0.75, 1])
quartis
 #visualização do desvio padrão
np.std(jogadores, ddof = 1)
# Visualização de estatísticas mais detalhadas usando a biblioteca scipy
stats.describe(jogadores)
