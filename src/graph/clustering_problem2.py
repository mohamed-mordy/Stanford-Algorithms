#!/usr/bin/env python3

import time
import UnionFind
from multiprocessing import pool


def compute_max_clusters(filename):
    t = time.time()
    with open(filename) as f:
        n_bits = int(f.readline().split()[1])
        # generate masks for computing one hamming distance
        masks = [(1 << n) for n in range(n_bits)]
        # generate masks for computing two hamming distance
        masks += [(1 << x | 1 << y) for x in range(n_bits) for y in range(x + 1, n_bits)]
        # reading the input into a set will take care of the duplicates by ignoring them
        s = set()
        for line in f:
            s.add(int(''.join(line.split()), 2))
        nodes = {}
        # construct a mapping of nodes --> IDs
        for i, node in enumerate(s):
            nodes[node] = i
        uf = UnionFind.UnionFind()
        for node in nodes.keys():
            for mask in masks:
                new_node = node ^ mask
                # look for nodes in the same cluster, and union them
                if new_node in nodes:
                    uf.union(nodes[node], nodes[new_node])
        # count the number of islands in the union-find, that is the total number of clusters
        return filename, len(set([uf.find(i) for i in range(len(nodes))])), time.time() - t


def main():
    # results = [2, 6, 2, 6118]
    # unit-test compute_mac_clusters
    files = [
        'clustering_problem2_testcases/clustering_test1.txt',
        'clustering_problem2_testcases/clustering_test2.txt',
        'clustering_problem2_testcases/clustering_test3.txt',
        'clustering_problem2_testcases/clustering_big.txt'
    ]
    p = pool.Pool(len(files))
    results = p.map(compute_max_clusters, files)
    for file, clusters, nSec in results:
        print(f'the file: {file} contains {clusters} cluster(s), the total running time is {nSec:.2} s')


if __name__ == '__main__':
    main()
