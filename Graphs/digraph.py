

class Digraph(object): # Adj. List

    def __init__(self, digraph: dict = {}) -> None:

        # self.digraph = digraph
        self.digraph = {node: {weight:0 for weight in neighbors} for node, neighbors in digraph.items()}
        print(self.digraph)

    def get_vertices(self) -> set:
        return set(self.digraph.keys())

    def get_edges(self) -> list:
        return self.create_edges()

    def set_edges(self, edge: tuple, weight: int = 0) -> None:
        if edge[0] in self.digraph:
            self.digraph[edge[0]].append(edge[1])
        else:
            self.digraph[edge[0]] = [edge[1]]

        self.digraph[edge[0][1]] = weight
        print(self.digraph)

    def vertice_exists(self):
        pass

    def create_edges(self) -> list:
        pass


# graph = {1:{}, 2:{}}
graph = {1: {1, 2, 3}, 2: {3}, 3: {1:0}}
graph[3].update({2:0})
print(graph)
digraph = Digraph(graph)

edge = (2, 1)
# digraph.set_edges(edge, 2)
# print(digrafo.get_vertices())


# https://codereview.stackexchange.com/questions/163414/adjacency-list-graph-representation-on-python
