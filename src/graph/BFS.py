#!/usr/bin/env python3

import Graph


class Vertex(Graph.Vertex):
    def __init__(self, name):
        super().__init__(name)
        self.distance = None
        self.explored = False


class BFS(Graph.Graph):
    def __init__(self):
        super().__init__()

    def bfs(self, s):
        self.vertices[s].explored = True
        self.vertices[s].distance = 0
        Q = [s]
        while Q:
            v = Q.pop(0)
            for tail, head in self.vertices[v].neighbors:
                if v == tail and not self.vertices[head].explred:
                    self.vertices[head].explored = True
                    self.vertices[head].distance = self.vertices[v].distance + 1
                    Q.append(head)

    def scc(self):
        n_components = 0
        for key, value in self.vertices.items():
            if not value.explored:  # not discovered yet
                self.bfs(key)
                n_components += 1
        return n_components


def bfs_test():
    pass
    # todo


def main():
    # bfs_test()
    pass


if __name__ == '__main__':
    main()
