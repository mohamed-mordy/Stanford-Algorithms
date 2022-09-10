#!/usr/bin/env python3


from matplotlib import pyplot
import itertools
import time
from multiprocessing import pool
import math
import copy

data = {}


def load_file(filename):
    with open(filename) as f:
        f.readline()
        global data
        data = {}
        for line in f:
            i, x, y = line.split()
            i = int(i)
            x = float(x)
            y = float(y)
            data[i] = (x, y)


def compute_min_tour(limit):
    def dest(x, y):
        return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    global data
    points = copy.copy(data)
    first = points[1]
    head_coor = points[1]
    head = 1
    del points[1]
    tour_len = 0.0
    while points:
        distances = []
        for (p, (x, y)), i in zip(points.items(), itertools.count()):
            if i == limit:
                break
            distances.append((dest(head_coor, (x, y)), p))
        distances.sort()
        tour_len += distances[0][0]
        head_coor = points[distances[0][1]]
        # head = distances[0][1]
        del points[distances[0][1]]
        if not points:
            tour_len += dest(head_coor, first)
        distances.clear()
    return limit, int(tour_len)


def plotter(filename):
    with open(filename) as fhandle:
        fhandle.readline()
        points = {}
        for line in fhandle:
            i, x, y = line.split()
            i = int(i)
            x = float(x)
            y = float(y)
            points[i] = (x, y)
            pyplot.plot(x, y, '.')
            pyplot.annotate(i, (x, y))
            if i == 50:
                break
    pyplot.show()


def main():
    load_file('nn.txt')
    limits = [x * 1000 for x in range(1, 4)]
    p = pool.Pool(len(limits))
    results = p.map(compute_min_tour, limits)
    for i, j in results:
        print(f'for a limit: {i}, the min_tour is: {j}')
    # plotter('nn.txt')
    pass


if __name__ == '__main__':
    main()
