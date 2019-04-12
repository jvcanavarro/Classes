class Grafo:
	def __init__(self, grafo=None):
		if not grafo:
			grafo = {}
		self.grafo = grafo

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        }