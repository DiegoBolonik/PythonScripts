# Importação da função para fazer o teste
from scipy.stats import t

# Qual a probabilidade de selecionar um cientista de dados e o salário ser menor que R$ 80 por hora
t.cdf(1.5, 8)
# Qual a probabilidade do salário ser maior do que 80?
t.sf(1.5, 8)
# Somatório da execução dos dois códigos acima (lado esquerdo + lado direito da distribuição)
t.cdf(1.5, 8) + t.sf(1.5, 8)
