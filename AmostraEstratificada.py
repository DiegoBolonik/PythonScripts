# Importação das bibliotecas: pandas para carregar arquivos .csv e train_test_split para divisão da base de dados (separar amostras)
import pandas as pd
from sklearn.model_selection import train_test_split

# Carregamento da base de dados e contagem de quantos registros existem por classe
iris = pd.read_csv('iris.csv')
iris['class'].value_counts()

# iris.iloc[:, 0:4]: buscamos somente os atributos previsores, ou seja, os dados sobre pétala e sétala da planta
# iris.iloc[:, 4]: buscamos somente a classe, que é a espécie da planta (setosa, virginica ou versicolor)
# test_size: selecionamos 50% da base de dados, que serão copiados para as variáveis X e Y. Essa função retorna 4 valores,
# porém, vamos usar somente os 50% da base de dados e por isso colocamos "_" para os outros valores
# stratify: para retornar a amostra baseada na classe
X, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4],
                              test_size = 0.5, stratify = iris.iloc[:,4])
y.value_counts()

# Carregamento da base de dados e contagem de quantos registros por classe
infert = pd.read_csv('infert.csv')
infert

infert['education'].value_counts()

# Criando uma amostra com somente 40% dos registros (por isso é definido 0.6, pois é gerado o inverso)
X1, _, y1, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1],
                                test_size = 0.6, stratify = infert.iloc[:, 1])
y1.value_counts()
