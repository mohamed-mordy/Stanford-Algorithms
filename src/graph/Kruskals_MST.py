#!/usr/bin/env python3

import collections
import UnionFind


Edge = collections.namedtuple('Edge', ['tail', 'head', 'cost'])


class KruskalsMST:
    def __init__(self):
        self.edges = []
        # self.T = set()
        self.min_cost = 0
        self.unionfind = UnionFind.UnionFind()

    def mst(self):
        self.edges.sort(key=lambda x: x.cost)
        for tail, head, cost in self.edges:
            if self.unionfind.find(tail) != self.unionfind.find(head):
                self.unionfind.union(tail, head)
                self.min_cost += cost
        return self.min_cost

    def add_edge(self, edge):
        self.edges.append(edge)


def test_kruskals_mst(filename):
    G = KruskalsMST()
    with open(filename) as fhandle:
        fhandle.readline()
        for line in fhandle:
            tail, head, cost = line.split()
            G.add_edge(Edge(int(tail), int(head), int(cost)))
    return G.mst()


def main():
    assert test_kruskals_mst('kruskals_testcases/edges_test1.txt') == 7, 'test one: failed'
    # print(test_kruskals_mst('kruskals_testcases/edges_test1.txt'))
    print('test one: passed')

    assert test_kruskals_mst('kruskals_testcases/edges.txt') == -3612829, 'test two: failed'
    # print(test_kruskals_mst('kruskals_testcases/edges.txt'))
    print('test two: passed')


if __name__ == '__main__':
    main()
