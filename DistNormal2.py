# Importação das bibliotecas: matplotlib para geração de gráficos
from scipy import stats
from scipy.stats import norm, skewnorm
import matplotlib.pyplot as plt

# Criação de uma variável com dados em uma distribuição normal com a função rvs (100 elementos)
dados = norm.rvs(size = 1000)
dados
#histograma
plt.hist(dados, bins = 20)
plt.title('Dados')
# Geração de gráfico para verificar se a distribuição é normal
fig, ax = plt.subplots()
stats.probplot(dados, fit=True,   plot=ax)
plt.show()
# Execução do teste de Shapiro
#segundo argumento é o valor de p, não há como rejeitar a hipótese nula
stats.shapiro(dados)
dados2 = skewnorm.rvs(4, size=1000)
#histograma
plt.hist(dados2, bins = 20)
plt.title('Dados')
# Geração de gráfico para verificar se a distribuição é normal
fig, ax = plt.subplots()
stats.probplot(dados2, fit=True,   plot=ax)
plt.show()
stats.shapiro(dados2)
