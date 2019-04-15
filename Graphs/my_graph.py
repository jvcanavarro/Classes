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

    def set_aresta(self, aresta):
        aresta = set(aresta)
        vertice = aresta.pop()
        if aresta:
            vertice2 = aresta.pop()
        else:
            vertice2 = vertice
        if vertice in self.__graph:
            self.__graph[vertice].append(vertice2)
        else:
            self.__graph[vertice] = [vertice2]

    def __gerar_arestas(self):
        arestas = []
        for vertice in self.__graph:
            for vizinho in self.__graph[vertice]:
                if {vizinho, vertice} not in arestas:
                    arestas.append({vertice, vizinho})
      
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