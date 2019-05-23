from collections import defaultdict as default

class Digraph:

	def __init__(self, digraph:dict = None) -> None:
		if not digraph:
			digraph = {}
		self.digraph = digraph

	def get_vertices(self) -> list:
		return list(self.digraph.keys())

	def get_arestas(self) -> list:
		return self.gera_arestas()

	def set_vertice(self, vertice) -> None:
		if vertice not in self.digraph:
			self.digraph[vertice] = []

	def set_aresta(self, aresta) -> None:
		aresta = set(aresta) # Set = Conjunto de elementos únicos.
		vertice = aresta.pop()
		if aresta:
			vertice2 = aresta.pop()
		else:
			vertice2 = vertice
		if vertice in self.digraph:
			self.digraph[vertice].append(vertice2)
		else:
			self.digraph[vertice] = [vertice2]


grafo = {1 : {1,2,3}, 2 : {3}, 3 : {1}}

graph = {}
s = dict((k,(r:0)) for k,r in grafo.items())
print(s)

# graph = default(dict)
# for key, value in grafo.items():
# 	graph[key] = {el:0 for el in value}

# print(graph)


digrafo = Digraph(grafo)
digrafo.set_vertice(4)

# https://codereview.stackexchange.com/questions/163414/adjacency-list-graph-representation-on-python
