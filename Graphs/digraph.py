

class Digraph(object):

    def __init__(self, digraph: dict = {}) -> None:
        self.digraph = digraph
        print(self.digraph)

    def get_vertices(self) -> set:
        return set(self.digraph.keys())

    def get_edges(self) -> list:
        return self.create_edges()

    def set_vertice(self, vertice: int) -> None:
        if vertice not in self.digraph:
            self.digraph[vertice] = []

    def set_edges(self, edge) -> None:
        edge = set(edge)  # Set = Conjunto de elementos únicos.
        vertice = edge.pop()
        if edge:
            vertice2 = edge.pop()
        else:
            vertice2 = vertice
        if vertice in self.digraph:
            self.digraph[vertice].append(vertice2)
        else:
            self.digraph[vertice] = [vertice2]

    def create_edges(self) -> list:
        pass


graph = {1: {1, 2, 3}, 2: {3}, 3: {1}}

# for key, value in grafo.items():
# 	print('key', key)
# 	print('value', value)
# 	graph[key] = {el:0 for el in value}


digrafo = Digraph(graph)

digrafo.set_vertice(4)

print(digrafo.get_vertices())


# https://codereview.stackexchange.com/questions/163414/adjacency-list-graph-representation-on-python
