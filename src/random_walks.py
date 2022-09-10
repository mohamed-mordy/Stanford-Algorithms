#!/usr/bin/env python3

import random
import itertools
from matplotlib import pyplot
from multiprocessing import pool


def random_walk_to(n):
    results = []
    for _ in range(10):
        current = 0
        c = itertools.count()
        while current != n:
            next(c)
            if current == 0:
                current = 1
                continue
            current = random.choice([current-1, current+1])
        results.append(next(c))
    avg = int(sum(results) / len(results))
    return n, avg


def main():
    data_lst = [x for x in range(10, 3000, 100)]
    p = pool.Pool(len(data_lst))
    return_lst = p.map(random_walk_to, data_lst)
    p.close()
    p.join()
    for i, j in return_lst:
        print(i, i ** 2, j)
        # pyplot.plot(i, j, '.')
    # pyplot.show()


if __name__ == '__main__':
    main()
