# João Victor da Silva Dias Canavarro - 201704940015

class Graph:
	#TODO: Adicionar Flag pra Grafo Direcionado.
	def __init__(self, graph=None):
		"""Inicia o Grafo por meio de um dicionário, fornecido ou não
		pelo usúario."""
		if not graph:
			graph = {}
		self.__graph = graph

	def get_vertices(self):
		return list(self.__graph.keys())

	def get_arestas(self):
		return self.__gerar_arestas()

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

	def __str__(self): # A função print chama essa.
		aux = "vertices: "
		for vertice in self.__graph:
			aux += str(vertice) + " " 

		aux += "\narestas:"
		for aresta in self.__gerar_arestas():
			aux += str(edge) + " "

		return aux

	def vertices_isolados(self):
		graph = self.__graph
		isolados = []
		for vertice in graph:
			print(isolados, vertice)
			if not graph[vertice]:
				isolados += [vertice]
		return isolados

	def vertice_grau(self, vertice):
		# O grau de um vértice é o número de arestas conectadas à ele.
		adjacentes = self.__graph[vertice]
		return len(adjacentes) + adjacentes.count(vertice)

	def dfs(self, inicio, vertices_visitados=None, tempo=0):
		if not vertices_visitados:
			vertices_visitados = set()

		vertices_visitados.add(inicio)

		for proximo in self.__graph[inicio] - vertices_visitados:
			dfs(proximo, vertices_visitados, tempo += 1)
		
		return vertices_visitados, tempo

	def bfs(self, inicio, vertices_visitados=None, tempo=0):
		if not vertices_visitados:
			vertices_visitados = set()

		fila = [inicio]
		while fila:
			vertice_atual = fila.pop(0)
			if vertice_atual not in vertices_visitados:
				vertices_visitados.add(vertice_atual)
				fila.extend(self.graph[vertice_atual] - vertices_visitados)
			tempo += 1
		return vertices_visitados, tempo


	def conexo(self, inicio=None):
		if not inicio:
			inicio = self.__graph[0]

		vertices_visitados, _ = dfs(inicio)
		return len(vertices_visitados) == len(self.__graph)

	def is_eulerian(self):
		# checar se é conexo
		for vertice in get_vertices():
			if vertice_grau(vertice) % 2 == 1: # ímpar
				return False
		return True

	def is_open_eulerian(self):
		# checar se é conexo
		vertices_impares = 0
		for vertice in get_vertices():
			if vertice_grau(vertice) % 2 == 1: # ímpar
			v	ertices_impares += 1
		return vertices_impares == 2

	def show_matrix_format(self):
		pass

	def show_list_format(self):
		pass