#!/usr/bin/env python3

import collections
import UnionFind

Edge = collections.namedtuple('Edge', ['tail', 'head', 'distance'])


class Clustering:
    def __init__(self):
        self.edges = []
        self.unionfind = UnionFind.UnionFind()

    def clustering(self, k):
        self.edges.sort(key=lambda x: x.distance)
        i = 0
        while self.unionfind.n_sets > k:
            tail, head, _ = self.edges[i]
            if self.unionfind.find(tail) != self.unionfind.find(head):
                self.unionfind.union(tail, head)
            i += 1
        while True:
            tail, head, _ = self.edges[i]
            if self.unionfind.xfind(tail) != self.unionfind.xfind(head):
                break
            i += 1
        return self.edges[i].distance

    def add_edge(self, edge):
        self.edges.append(edge)


def test_clustering(filename, k):
    G = Clustering()
    with open(filename) as fhandle:
        n_nodes = fhandle.readline()
        [G.unionfind.find(i) for i in range(1, int(n_nodes) + 1)]
        for line in fhandle:
            tail, head, distance = line.split()
            G.add_edge(Edge(int(tail), int(head), int(distance)))
    return G.clustering(k)


def main():
    assert test_clustering('clustering_testcases/input_completeRandom_10_32.txt', 4) == 90, 'test one failed'
    print('test one: pass')
    assert test_clustering('clustering_testcases/input_completeRandom_11_32.txt', 4) == 100, 'test two failed'
    print('test two: pass')
    assert test_clustering('clustering_testcases/clustering.txt', 4) == 106, 'test three failed'
    print('test three: pass')


if __name__ == '__main__':
    main()
