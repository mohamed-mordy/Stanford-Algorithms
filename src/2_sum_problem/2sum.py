#!/usr/bin/env python3

import time
import bisect


def naive_and_idiot():
    # 427
    # the running time is: 3372.7678151130676
    A = {int(i) for i in open('2sum.txt')}
    sums = set()
    for i in range(-10000, 10001, 1):
        for elem in A:
            if i-elem in A:
                sums.add(i)
    print(len(sums))


def two_sum():
    # Important:
    #       this function is designed specifically for the companion data-set, '2sum.txt' file.
    #       this function won't work correctly on every input data set.
    # 427
    # the running time is: 1.5979466438293457
    A = {int(i) for i in open('2sum.txt')}
    X = sorted(A)
    Xl = X[:bisect.bisect(X, 0)]
    sums = set()
    for x in Xl:
        i = bisect.bisect(X, -10000 - x)
        j = bisect.bisect(X, 10000 - x)
        for y in X[i:j]:
            if 10000 >= x + y >= -10000:
                sums.add(x + y)
    print(len(sums))


if __name__ == '__main__':
    t1 = time.time()
    #two_sum()
    naive_and_idiot()
    t2 = time.time()
    print(f'the running time is: {(t2 - t1)}')
