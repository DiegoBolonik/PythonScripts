# Importação das bibliotecas
import pandas as pd
import seaborn as srn
import matplotlib.pyplot as plt

# Carregamento da base de dados
base = pd.read_csv('co2.csv')
base.head()
# Gráfico de dispersão utilizando os atributos conc e uptake, agrupamento pelo type
srn.scatterplot(base.conc, base.uptake, hue = base.Type)
# Seleção de registros específicos da base de dados (Quebec e Mississipi)
q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']
# Subgráfico (1 linha e duas colunas) mostrando gráficos sobre cada região
plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(q.conc, q.uptake).set_title('Quebec')
plt.subplot(1,2,2)
srn.scatterplot(m.conc, m.uptake).set_title('Mississippi')
plt.tight_layout()
# Refrigerado e não refrigerado
ch = base.loc[base['Treatment'] == 'chilled']
nc = base.loc[base['Treatment'] == 'nonchilled']
# Gráfico somente com 'chilled' e 'nonchilled'
plt.figure()
plt.subplot(1,2,1)
srn.scatterplot(ch.conc, ch.uptake).set_title('Chilled')
plt.subplot(1,2,2)
srn.scatterplot(nc.conc, nc.uptake).set_title('Non chilled')
plt.tight_layout()
# Carregamento de outro arquivo, cancer de esofago
base2 = pd.read_csv('esoph.csv')
base2
# Gráfico entre os atributos 'alcgp' e 'ncontrols'
srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, jitter = False)
# Gráfico entre os atributos 'alcgp' e 'ncontrols', com agrupamento
srn.catplot(x = 'alcgp', y = 'ncontrols', data = base2, col = 'tobgp')
