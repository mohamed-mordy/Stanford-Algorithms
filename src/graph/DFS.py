#!/usr/bin/env python3


import Graph


class Vertex(Graph.Vertex):
    def __init__(self, name):
        super(Vertex, self).__init__(name)
        self.explored = False


class DFS(Graph.Graph):

    def __init__(self):
        super().__init__()

    def dfs(self, s):
        """ General purpose dfs() algorithm"""
        self.vertices[s].explored = True
        stack = [s]
        while stack:
            v = stack.pop()
            for tail, head in self.vertices[v].neighbors:
                if tail == v and not self.vertices[head].explored:
                    self.vertices[head].explored = True
                    stack.append(head)


def test_dfs():
    print("Hello, World!\n")
    G = DFS()
    G.add_vertex(Vertex(1))
    G.add_vertex(Vertex(2))
    G.add_vertex(Vertex(3))
    G.add_vertex(Vertex(4))
    G.add_vertex(Vertex(5))
    G.add_vertex(Vertex(6))
    G.add_edge(Graph.Edge(1, 2))
    G.add_edge(Graph.Edge(1, 3))
    G.add_edge(Graph.Edge(1, 4))
    G.add_edge(Graph.Edge(2, 5))
    G.add_edge(Graph.Edge(3, 5))
    G.add_edge(Graph.Edge(4, 6))
    G.add_edge(Graph.Edge(5, 6))
    G.print()
    print()
    G.dfs(1)
    G.print()


def main():
    test_dfs()


if __name__ == '__main__':
    main()
