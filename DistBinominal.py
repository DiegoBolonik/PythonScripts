# Importação da função binom
from scipy.stats import binom

# Jogar uma moeda 5 vezes, qual a probabilidade de dar cara 3 vezes?
# eventos , experimentos, probabilidades
prob = binom.pmf(3, 5, 0.5)
prob

# Passar por 4 sinais de 4 tempos, qual a probabilidade de pegar sinal verde
# nenhuma, 1, 2, 3 ou 4 vezes seguidas?
binom.pmf(0, 4, 0.25) + binom.pmf(1, 4, 0.25) + binom.pmf(2, 4, 0.25) + binom.pmf(3, 4, 0.25) + binom.pmf(4, 4, 0.25)

# E se forem sinais de dois tempos?
binom.pmf(4, 4, 0.5)

# Probabilidade acumulativa
binom.cdf(4, 4, 0.25)

# Concurso com 12 questões, qual a probabilidade de acertar 7 questões considerando
# que cada questão tem 4 alternativas?
binom.pmf(7, 12, 0.25) 

# Probabilidade de acertar as 12 questões
binom.pmf(12, 12, 0.25) 
