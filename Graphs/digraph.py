# João Victor da Silva Dias Canavarro - 201704940015
import numpy as np
from collections import defaultdict

class Digraph(object): # Adj. List
    """
    A class used to represent a directed graph using adjacency list
    ...
    Atributes
    ---------
    self.digraph organized as nested dictionaries
    {node1: {neighbor1: weight1, neighbor2: weight2}, node2: {}, ...}
    Example:
        self.digraph = {1: {1, 2, 3}, 2: {3}, 3: {1: 0}}
    self.edges organized as a list of tuples
    [(vertice1 -> vertice2), (vertice5 -> vertice2), (vertice3 -> vertice3), ...]
    Example:
        self.edges = [(1, 1), (1, 2), (1, 3), (2, 3), (3, 1), (4, 1)]

    Methods
    -------

    """

    def __init__(self, digraph: dict = {}) -> None:
        # self.digraph = {node: {weight:0 for weight in neighbors} for node, neighbors in digraph.items()}
        self.digraph = defaultdict(dict, digraph)

    def matrix_representation(self) -> list:
        n = len(adj_list)
        adj_matrix = np.nan * np.ones((n,n))
        np.fill_diagonal(adj_matrix,0)
        for i in range(n):
            for j, w in adj_list[i]:
                adj_matrix[i,j] = w
        return adj_matrix

    def get_vertices(self) -> set:
        return set(self.digraph.keys())

    def get_edges(self) -> list:
        self.edges = [(vertice, neighbor) for vertice in self.digraph for neighbor in self.digraph[vertice]]
        # equal to:
        # for vertice in self.digraph:
        #     for neighbor in self.digraph[vertice]:
        #             edges.append((vertice, neighbor))
        return self.edges

    def set_edges(self, edge: tuple) -> None:
        # edge = (vertice1 -> vertice2)

        if edge[1] not in self.digraph:
            self.digraph[edge[1]] = {}

        if edge[0] in self.digraph:
            self.digraph[edge[0]].add(edge[1])
        else:
            self.digraph[edge[0]] = {edge[1]}

    def warshall_transitive_closure(self) -> dict:
        pass





    # Magic Functions
    def __iter__(self):
        return iter(self.digraph.keys())

    def __len__(self):
        return len(self.digraph)

# graph = {1:{}, 2:{}}
graph = {1: {1, 2, 3}, 2: {3}, 3: {1: 0}}
digraph = Digraph(graph)

# edge = (2, 1, 0)
# edge = {2: {1: 0}}

edge = (1, 4)
digraph.set_edges(edge)
# digraph.create_edges()
print(digraph.get_edges())
print(digraph.get_vertices())