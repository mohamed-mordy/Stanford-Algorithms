#!/usr/bin/env python3

import Graph
import collections
import heapq
from math import inf

Edge = collections.namedtuple('Edge', ['tail', 'head', 'length'])


class Vertex(Graph.Vertex):
    def __init__(self, name):
        super().__init__(name)
        # self.pred = None
        # self.dist = inf

    def add_neighbor(self, edge):
        if isinstance(edge, Edge):
            self.neighbors.add(edge)


class Dijkstra(Graph.Graph):
    def __init__(self):
        super().__init__()
        self.A = {}
        # todo

    def dijkstra_naive(self, s):
        X = {s}
        V_X = set([x for x in range(1, len(self.vertices) + 1)])
        V_X.remove(s)
        self.A = {i: inf for i in range(1, len(self.vertices) + 1)}
        self.A[s] = 0
        for edge in self.vertices[s].neighbors:
            if self.A[edge.tail] + edge.length < self.A[edge.head]:
                self.A[edge.head] = self.A[edge.tail] + edge.length
        while V_X:
            min_dist = inf
            the_edge = None
            for vertex in self.vertices.values():
                for edge in vertex.neighbors:
                    if edge.tail in X and edge.head in V_X and self.A[edge.tail] + edge.length < min_dist:
                        the_edge = edge
                        min_dist = self.A[edge.tail] + the_edge.length
            X.add(the_edge.head)
            V_X.remove(the_edge.head)
            for edge in self.vertices[the_edge.head].neighbors:
                if self.A[edge.tail] + edge.length < self.A[edge.head]:
                    self.A[edge.head] = self.A[edge.tail] + edge.length

    def dijkstra_priority_queue(self, s):
        # todo
        pass

    def print(self):
        for key in sorted(self.vertices.keys()):
            print(f'vertex {key}:')
            for edge in self.vertices[key].neighbors:
                print('\t\t', edge)

    def add_edge(self, edge):
        if edge.tail in self.vertices and edge.head in self.vertices:
            self.vertices[edge.tail].add_neighbor(edge)
            if self.directed:
                self.vertices[edge.head].add_neighbor(edge)
            else:
                self.vertices[edge.head].add_neighbor(Edge(edge.head, edge.tail, edge.length))
            return True
        else:
            return False


def test_dijkstra(filename, n_vertices):
    G = Dijkstra()
    print('constructing the vertices\n')
    for i in range(1, n_vertices + 1):
        G.add_vertex(Vertex(i))
    print('constructing the edges\n')
    with open(filename) as input_file:
        for line in input_file:
            tail, *other = line.split()
            for pair in other:
                head, length = pair.split(',')
                G.add_edge(Edge(int(tail), int(head), int(length)))
    print('printing the graph to the output')
    G.dijkstra_naive(1)
    # G.print()
    for key in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        print(G.A[key], end=',')
    print()

    # for key in sorted(G.A.keys()):
    #     print(f'{key} : {G.A[key]}')


def main():
    test_dijkstra('dijkstra_testcases/dijkstraData.txt', 200)
    # test_dijkstra('dijkstra_testcases/dijkstraData_test1.txt', 10)
    # test_dijkstra('dijkstra_testcases/dijkstraData_test2.txt', 8)


if __name__ == '__main__':
    main()
