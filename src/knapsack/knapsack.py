#!/usr/bin/env python3

import time


#@profile
def compute_optimal_solution_value_straightforward(filename):
    with open(filename) as f:
        W, n = f.readline().split()
        W, n = int(W), int(n)
        values = {}
        weights = {}
        for i, line in enumerate(f, 1):
            v, w = line.split()
            values[i] = int(v)
            weights[i] = int(w)
    A = {i: {} for i in range(n + 1)}
    A[0] = {x: 0 for x in range(W + 1)}
    for i in range(1, n + 1):
        for x in range(W + 1):
            if x < weights[i]:
                A[i][x] = A[i - 1][x]
            else:
                A[i][x] = max(A[i - 1][x], A[i - 1][x - weights[i]] + values[i])
        if i > 2:
            del A[i - 2]
    return A[n][W]


def compute_optimal_solution_value_tricky(filename):
    pass


def main():
    assert compute_optimal_solution_value_straightforward('test1.txt') == 8
    assert compute_optimal_solution_value_straightforward('test2.txt') == 147
    assert compute_optimal_solution_value_straightforward('test3.txt') == 14621
    assert compute_optimal_solution_value_straightforward('knapsack1.txt') == 2493893

    # Warning: running time is 55 min, need more elegant algorithm
    assert compute_optimal_solution_value_straightforward('knapsack_big.txt') == 4243395
    pass


if __name__ == '__main__':
    main()
