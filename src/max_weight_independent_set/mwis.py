#!/usr/bin/env python3


def compute_max_weight_independent_set(filename):
    with open(filename) as f:
        f.readline()
        w = {}
        for i, v in enumerate(f, 1):
            w[i] = int(v)
    A = {0: 0, 1: w[1]}
    for i in range(2, len(w) + 1):
        A[i] = max(A[i - 1], A[i - 2] + w[i])
    s = set()
    i = len(w)
    while i >= 1:
        if A[i - 1] >= A.get(i - 2, 0) + w[i]:
            i -= 1
        else:
            s.add(i)
            i -= 2
    return_str = ''
    for i in [1, 2, 3, 4, 17, 117, 517, 997]:
        return_str += (str(1) if i in s else str(0))
    return return_str


def main():
    assert compute_max_weight_independent_set('test1.txt') == '01011011'
    assert compute_max_weight_independent_set('mwis.txt') == '10100110'


if __name__ == '__main__':
    main()
