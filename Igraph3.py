# Importação das bibliotecas
from igraph import Graph
from igraph import plot

# recriamos o grafo 4
grafo4 = Graph(directed = False)
grafo4.add_vertices(5)
grafo4.add_edges([(0,1),(1,2),(2,3),(3,4),(4,0),(0,2),(2,1)])
grafo4.add_vertex(5)
grafo4.add_vertex(6)
grafo4.vs['label'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
grafo4.vs['name'] = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Impressão da matriz de adjacência
print(grafo4.get_adjacency())
# linha
grafo4.get_adjacency()[0,]
#linha e coluna
grafo4.get_adjacency()[0,1]
# Estrutura de repetição para percorrer cada vértice, visualizando o nome e o rótulo
for v in grafo4.vs:
   print(v) 
plot(grafo4, bbox=(0,0,300,300))

# Criação de grafo com pesos entre as relações
grafo5 = Graph(edges = [(0,1),(2,3),(0,2),(0,3)], directed = True)
grafo5.vs['label'] = ['Fernando', 'Pedro', 'Jose', 'Antonio']
grafo5.vs['peso'] = [40,30,30,25]
print(grafo5)
# Percorrer os vértices para visualizar os pesos
for v in grafo5.vs:
    print(v)
grafo5.vs[0]

# Definição do tipo de amizado e do peso das relações
grafo5.es['TipoAmizade'] = ['Amigo', 'Inimigo', 'Inimigo', 'Amigo']
grafo5.es['weight'] = [1,2,1,3]
print(grafo5)

# Percorrer os vértices, tipo de amizade
for e in grafo5.es:
    print(e)
#propriedades e valores de uma posição
grafo5.es[0]
# tipos de amizade
grafo5.es['TipoAmizade']
print(grafo5)

# Mudança dos tipos das relações em grafos já existentes
grafo5.vs['type'] = 'Humanos'
grafo5.vs['name'] = 'Amizades'
print(grafo5)
plot(grafo5, bbox=(0,0,300,300)) 
