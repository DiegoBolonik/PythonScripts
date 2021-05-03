# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Carregamento da base de dados
base = pd.read_csv('co2.csv')
base.head()
#criando duas variáveis para cada atributo (x = conc e y = uptake)
x = base.conc
y = base.uptake
# Retorna os valores únicos do atributo "treatment"
unicos = list(set(base.Treatment))
unicos
# Percorre cada tipo de tratamento (chilled e nonchilled) e cria um gráfico de dispersão
for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i])
plt.legend(loc = 'lower right')
