#!/usr/bin/env python3

import Graph
import collections
import heapdict
import math
import random

Edge = collections.namedtuple('Edge', ['tail', 'head', 'cost'])


class Vertex(Graph.Vertex):
    def __init__(self, name):
        super().__init__(name)

    def add_neighbor(self, edge):
        """ Add a neighbor to this Vertex,
        the input argument should be a literal"""
        if isinstance(edge, Edge):
            self.neighbors.add(edge)


class PrimsMST(Graph.Graph):
    def __init__(self):
        super().__init__()
        self.X = set()
        self.T = 0
        self.heap = heapdict.heapdict()

    def mst(self):
        # preprocessing step
        s = random.choice(list(self.vertices.keys()))
        self.X.add(s)
        for vertex in self.vertices.keys():
            if vertex != s:
                self.heap[vertex] = math.inf
        for _, head, cost in self.vertices[s].neighbors:
            self.heap[head] = cost
        # end of the preprocessing step
        while self.heap:
            s, cost = self.heap.popitem()
            self.T += cost
            self.X.add(s)
            for _, head, _ in self.vertices[s].neighbors:
                min_cost = math.inf
                if head not in self.X:
                    for _, h, c in self.vertices[head].neighbors:
                        if h in self.X and c < min_cost:
                            min_cost = c
                    self.heap[head] = min_cost
        return self.T

    def add_edge(self, edge):
        if edge.tail in self.vertices and edge.head in self.vertices:
            self.vertices[edge.tail].add_neighbor(edge)
            if self.directed:
                self.vertices[edge.head].add_neighbor(edge)
            else:
                self.vertices[edge.head].add_neighbor(Edge(edge.head, edge.tail, edge.cost))
            return True
        else:
            return False


def test_prims_mst(filename):
    G = PrimsMST()
    with open(filename) as fhandle:
        nodes, edges = fhandle.readline().split()
        for i in range(1, int(nodes) + 1):
            G.add_vertex(Vertex(i))
        for line in fhandle:
            tail, head, cost = line.split()
            G.add_edge(Edge(int(tail), int(head), int(cost)))
    return G.mst()


def main():
    assert test_prims_mst('prims_testcases/edges_test1.txt') == 7, 'test failed'
    print('test one: pass')
    assert test_prims_mst('prims_testcases/edges.txt') == -3612829, 'test failed'
    print('test two: pass')


if __name__ == '__main__':
    main()
