# Importação das funções, chi2_contingency porque temos 2 categorias
import numpy as np
from scipy.stats import chi2_contingency

# Criação da matriz com os dados e execução do teste
novela = np.array([[19, 6], [43, 32]])
novela
#segundo valor é o pvalue
#Valor de p é maior que 0,05 não há evidências de diferença significativa (hipótese nula): não há diferença significativa
chi2_contingency(novela)
novela2 = np.array([[22, 3], [43, 32]])
novela2
#agora valor de p menor que 0,05, podemos rejeitar a hipótese nula em favor da hipótese alternativa: há diferença significativa
chi2_contingency(novela2)
