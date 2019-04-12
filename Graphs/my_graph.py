class Graph:

    def __init__(self, graph=None):
        """Inicia o Grafo por meio de um dicionário, fornecido ou não
        pelo usúario."""
        if not graph:
            graph = {}
        self.__graph = graph

    def get_vertices(self):
        return list(self.__graph.keys())

    def get_arestas(self):
        pass

    def set_vertice(self, vertice):
        """Primeiro checa se ja existe dado vértice, senão adiciona ao
        grafo com uma lista vazia como valor."""
        if vertice not in self.__graph:
            self.__graph[vertice] = []
# graph = {'A': [1,2], 'B': [2,3], 'C': [3,1]}
graph =  { "a" : ["d"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : []
    }
my_graph = Graph(graph)
print(my_graph.get_vertices())