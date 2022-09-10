#!/usr/bin/env python3

import Graph


class Vertex(Graph.Vertex):
    # TODO
    def __init__(self, name):
        super().__init__(name)
        self.f = 0
        self.explored = False

    def __repr__(self):
        return str(self.name) + ': explored? str(self.explored)' + f' f = {self.f} '+" --> " + str(self.neighbors)


class TopologicalSort(Graph.Graph):

    def __init__(self):
        super().__init__(directed=True)
        self.current_label = 0

    def topological_sort(self):  # this is DFS_Loop
        """ sort the graph topologically, given the graph is acyclic"""
        # mark all nodes unexplored -> implicitly done at initialization
        self.current_label = len(self.vertices)
        for key, value in self.vertices.items():
            if not value.explored:  # i.e., not yet explored
                self.__DFS__(value.name)

    def __DFS__(self, s):
        """ DFS: to be used specifically for topological sorting"""
        self.vertices[s].explored = True
        for tail, head in self.vertices[s].neighbors:
            if tail == s and not self.vertices[head].explored:
                self.__DFS__(head)
        self.vertices[s].f = self.current_label
        self.current_label -= 1

    # def print(self):
    #     # TODO
    #     pass


def test_topological_sort():
    G = TopologicalSort()
    G.add_vertex(Vertex('S'))
    G.add_vertex(Vertex('V'))
    G.add_vertex(Vertex('W'))
    G.add_vertex(Vertex('T'))
    G.add_edge(Graph.Edge('S', 'V'))
    G.add_edge(Graph.Edge('S', 'W'))
    G.add_edge(Graph.Edge('V', 'T'))
    G.add_edge(Graph.Edge('W', 'T'))
    G.print()
    G.topological_sort()
    print()
    G.print()


def main():
    test_topological_sort()


if __name__ == '__main__':
    main()
