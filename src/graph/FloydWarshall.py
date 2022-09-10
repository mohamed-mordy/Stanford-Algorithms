#!/usr/bin/env python3

from sys import exit
from math import inf
import numpy as np
import os
import time
from multiprocessing import pool


class FloydWarshall:
    def __init__(self, n):
        self.vertices = set([x for x in range(1, n + 1)])
        self.n = n
        self.edges = {}

    def add_edge(self, tail, head, cost):
        assert tail in self.vertices and head in self.vertices
        if (tail, head) in self.edges:
            self.edges[(tail, head)] = min(self.edges[(tail, head)], cost)
            return True
        else:
            self.edges[(tail, head)] = cost
            return True

    def floyd_warshall(self):
        n = self.n
        A = np.empty((2, n + 1, n + 1), dtype=np.float64)
        A.fill(inf)
        for i in self.vertices:
            for j in self.vertices:
                if i == j:
                    A[0, i, j] = 0
                elif (i, j) in self.edges:
                    A[0, i, j] = self.edges[(i, j)]
                else:
                    A[0, i, j] = inf
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    A[k % 2, i, j] = min(A[(k - 1) % 2, i, j], A[(k - 1) % 2, i, k] + A[(k - 1) % 2, k, j])
        return A[k % 2, :, :].min()
        pass


def test_floyd_warshall(filename):
    with open(filename) as fhandle:
        n, m = (int(x) for x in fhandle.readline().split())
        G = FloydWarshall(n)
        for line in fhandle:
            tail, head, cost = (int(x) for x in line.split())
            G.add_edge(tail, head, cost)
    m = G.floyd_warshall()
    print(f'the min of: {filename} is: {str(m)}')
    return m

    pass


def main():
    lst = ['apsp_testcases/g1.txt','apsp_testcases/g2.txt','apsp_testcases/g3.txt']
    p = pool.Pool(len(lst))
    p.map(test_floyd_warshall, lst)
    exit()
    # # assert test_floyd_warshall('apsp_testcases/test1.txt') == -41
    # # print('success')
    # # t = time.time()
    # # assert test_floyd_warshall('apsp_testcases/test2.txt') == -3127
    # # print('success')
    # # print(f'running time is {time.time() - t}')
    # return 0
    pass


if __name__ == '__main__':
    exit(main())
