#!/usr/bin/env python3

import heapq


def compute_min_max_code_length(filename):
    with open(filename) as f:
        f.readline()
        sym_weights = []
        for i, w in enumerate(f, 1):
            sym_weights.append((int(w), str(i)))
    heapq.heapify(sym_weights)
    depth_map = {}
    while len(sym_weights) > 2:
        s1 = heapq.heappop(sym_weights)
        s2 = heapq.heappop(sym_weights)
        s3 = (s1[0] + s2[0], s1[1] + '_' + s2[1])
        for s in s3[1].split('_'):
            depth_map[s] = depth_map.get(s, 0) + 1
        heapq.heappush(sym_weights, s3)
    assert len(sym_weights) == 2
    s1 = heapq.heappop(sym_weights)
    s2 = heapq.heappop(sym_weights)
    s3 = (s1[0] + s2[0], s1[1] + '_' + s2[1])
    for s in s3[1].split('_'):
        depth_map[s] = depth_map.get(s, 0) + 1
    v = sorted(depth_map.values())
    return v[0], v[-1]


def main():
    print(compute_min_max_code_length('test1.txt'))  # 2, 5
    print(compute_min_max_code_length('test2.txt'))  # 3, 6
    print(compute_min_max_code_length('test3.txt'))  # 2, 4
    print(compute_min_max_code_length('test4.txt'))  # 12, 26
    print(compute_min_max_code_length('huffman.txt'))  # 9, 19
    pass


if __name__ == '__main__':
    main()
