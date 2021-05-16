# Importação das bibliotecas
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import MultiComparison

# Carregamento da base de dados
tratamento = pd.read_csv('anova.csv', sep = ';')
tratamento.head()
# Boxplot agrupando os dados pelo remédio
tratamento.boxplot(by = 'Remedio', grid = False)
# Criação do modelo de regressão linear e execução do teste
modelo1 = ols('Horas ~ Remedio', data = tratamento).fit()
resultados1 = sm.stats.anova_lm(modelo1)
# Observar valor de p maior que 0,05 (Pr(>F)) Hipótese nula de que não há diferença significativa
resultados1

# Criação do segundo modelo utilizando mais atributos e execução do teste
modelo2 = ols('Horas ~ Remedio * Sexo', data = tratamento).fit()
resultados2 = sm.stats.anova_lm(modelo2)
#Nenhum valor de P mostra diferença significativa
resultados2

#Se houver diferença o teste de Tukey é executado
# Execução do teste de Tukey e visualização dos gráficos com os resultados
mc = MultiComparison(tratamento['Horas'], tratamento['Remedio'])
resultado_teste = mc.tukeyhsd()
print(resultado_teste)
resultado_teste.plot_simultaneous()
