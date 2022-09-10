#!/usr/bin/env python3

import Graph
import time
import resource
import sys
import os
from multiprocessing import pool


def optimize_for_recursive_approach():
    sys.setrecursionlimit(10 ** 6)
    resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


class Vertex(Graph.Vertex):
    def __init__(self, name):
        super().__init__(name)
        self.explored = False


class SCC(Graph.Graph):

    def __init__(self):
        super().__init__(directed=True)
        self.leaders = {}
        self.finishing_times = {}
        self.t = 0
        self.s = None

    def set_all_unexplored(self):
        """ Set all the Vertices in The Graph unexplored"""
        for value in self.vertices.values():
            value.explored = False

    def two_sat(self):
        self.__kosaraju_dfs_loop_1st__()
        self.set_all_unexplored()
        self.__kosaraju_dfs_loop_2nd__()
        scc = {}
        leaders = set([l for l in self.leaders.values()])
        for leader in leaders:
            scc[leader] = set()
        # don't need leaders anymore, I do this just for clarity
        del leaders
        for vertex, leader in self.leaders.items():
            scc[leader].add(vertex)
        for component in scc.values():
            for vertex in component:
                # this implementation is for specific data-set
                if -vertex in component:
                    return False
        return True

    def kosaraju(self):
        self.__kosaraju_dfs_loop_1st__()
        self.set_all_unexplored()
        self.__kosaraju_dfs_loop_2nd__()
        print(self.leaders)
        scc = {}
        for value in self.leaders.values():
            scc[value] = scc.get(value, 0) + 1
        return ",".join(str(i) for i in (sorted(scc.values(), reverse=True)[:5]))

    def __kosaraju_dfs_loop_1st__(self):
        self.t = 0
        for vertex in self.vertices.values():
            if not vertex.explored:
                # self.__kosaraju_dfs_iterative_1st__(vertex.name)
                self.__kosaraju_dfs_recursive_1st__(vertex.name)

    def __kosaraju_dfs_recursive_1st__(self, i):
        self.vertices[i].explored = True
        for tail, head in self.vertices[i].neighbors:
            if head == i and not self.vertices[tail].explored:
                self.__kosaraju_dfs_recursive_1st__(tail)
        self.t += 1
        self.finishing_times[self.t] = i

    def __kosaraju_dfs_iterative_1st__(self, i):
        self.vertices[i].explored = True
        stack = [i]
        while stack:
            v = stack[-1]
            flag = True
            for tail, head in self.vertices[v].neighbors:
                if head == v and not self.vertices[tail].explored:
                    self.vertices[tail].explored = True
                    stack.append(tail)
                    flag = False
            if flag:
                self.t += 1
                self.finishing_times[self.t] = v
                stack.pop()

    def __kosaraju_dfs_loop_2nd__(self):
        self.s = None
        # sort vertices by finishing times
        for _, vertex in sorted(self.finishing_times.items(), reverse=True):
            if not self.vertices[vertex].explored:
                # set current vertex to be a leader vertex
                self.s = vertex
                # call dfs() from the right place (i.e., current vertex)
                self.__kosaraju_dfs_recursive_2nd__(vertex)
                # self.__kosaraju_dfs_iterative_2nd__(vertex)

    def __kosaraju_dfs_recursive_2nd__(self, i):
        self.vertices[i].explored = True
        # set the leader of current vertex to be s
        self.leaders[i] = self.s
        for tail, head in self.vertices[i].neighbors:
            if tail == i and not self.vertices[head].explored:
                self.__kosaraju_dfs_recursive_2nd__(head)

    def __kosaraju_dfs_iterative_2nd__(self, i):
        self.vertices[i].explored = True
        stack = [i]
        while stack:
            v = stack.pop()
            self.leaders[v] = self.s
            for tail, head in self.vertices[v].neighbors:
                if tail == v and not self.vertices[head].explored:
                    self.vertices[head].explored = True
                    stack.append(head)


def test_two_sat(filename):
    G = SCC()
    with open(filename) as f:
        f.readline()
        for line in f:
            x, y = [int(x) for x in line.split()]
            G.add_vertex(Vertex(x))
            G.add_vertex(Vertex(-x))
            G.add_vertex(Vertex(y))
            G.add_vertex(Vertex(-y))
            G.add_edge(Graph.Edge(-x, y))
            G.add_edge(Graph.Edge(-y, x))
    return G.two_sat()


def test_kosaraju(filename, n_vertices):
    G = SCC()
    for i in range(1, n_vertices + 1):
        G.add_vertex(Vertex(i))
    with open(filename) as infile:
        for line in infile:
            tail, head = [int(s) for s in line.split()]
            G.add_edge(Graph.Edge(tail, head))
    # G.print()
    return G.kosaraju()


def main():
    optimize_for_recursive_approach()  # if recursive is used, otherwise, doesn't matter!
    # print(test_two_sat('2sat_testcases/test2.txt'))
    # exit()
    #
    #



    t1 = time.time()
    two_sat_filenames = ['2sat_testfiles/' + file for file in os.listdir('2sat_testfiles')]
    two_sat_filenames.sort()
    p = pool.Pool(len(two_sat_filenames))
    results = p.map(test_two_sat, two_sat_filenames)
    print(''.join(str(int(res)) for res in results))
    print(f'running time is {time.time() - t1 :.2f} sec')



    # x = test_kosaraju("scc_testcases/SCC.txt", 875714)  # 434821,968,459,313,211
    # assert test_kosaraju("scc_testcases/SCC.txt", 875714) == '434821,968,459,313,211'
    # x = test_kosaraju("scc_testcases/scc1.txt", 12)  # 5,4,3
    # x = test_kosaraju("scc_testcases/scc2.txt", 16)  # 7,4,4,1
    # x = test_kosaraju("scc_testcases/scc3.txt", 17)  # 8,4,4,1
    # print(f'the running time is: {(time.time() - t1):.3f} s')
    # return 0


if __name__ == '__main__':
    sys.exit(main())
