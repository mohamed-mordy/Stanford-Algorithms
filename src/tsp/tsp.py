#!/usr/bin/env python3

from matplotlib import pyplot
import itertools
import math


def compute_shortest_tour(filename):
    pass


def plotter(filename):
    with open(filename) as fhandle:
        n = int(fhandle.readline())
        X = []
        Y = []
        for i, line in enumerate(fhandle, 1):
            x, y = [float(x) for x in line.split()]
            X.append(x)
            Y.append(y)
            # pyplot.plot(x, y, '.')
            # pyplot.annotate(i, (x, y))
    # pyplot.plot(X, Y, '.')
    points = list(zip(X, Y))
    # points.sort(key=lambda p: p[0])
    # points.sort(key=lambda p: p[1])
    for i, (x, y) in enumerate(points, 1):
        pyplot.plot(x, y, '.')
        pyplot.annotate(i, (x, y))
    pyplot.grid()
    pyplot.show()


def pessimistic(filename):
    points = {}
    distances = {}
    with open(filename) as f:
        f.readline()
        for i, line in enumerate(f, 1):
            x, y = [float(x) for x in line.split()]
            points[i] = (x, y)
    for x, y in itertools.combinations(points.keys(), 2):
        x1, y1 = points[x]
        x2, y2 = points[y]
        distances[(x, y)] = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    lst = [(1, 2), (2, 6), (6, 10), (10, 11), (11, 12), (12, 15)
           , (15, 19), (18, 19), (18, 22), (22, 23), (21, 23), (17, 21), (17, 20), (20, 25), (24, 25)
           , (16, 24), (14, 16), (13, 14), (9, 13), (7, 9), (3, 7), (3, 4), (4, 8), (5, 8), (1, 5)]
    s = 0
    for d in lst:
        s += distances[d]
    return int(s)

    pass


def main():
    plotter('tsp.txt')
    # print(pessimistic('tsp.txt'))
    pass


if __name__ == '__main__':
    main()
