#!/usr/bin/env python3

import random


def data_generator():
    processing_times = set([random.randint(100, 1000) for _ in range(1000)])
    deadlines = set([random.randint(100, 1000) for _ in range(1000)])

    processing_times = list(processing_times)
    deadlines = list(deadlines)

    random.shuffle(deadlines)
    random.shuffle(processing_times)

    jobs = list(zip(processing_times, deadlines))
    # with open('jobs.txt', 'w') as fhandle:
    #     for p, d in jobs:
    #         fhandle.write(f'{p} {d}\n')

    return jobs


def schedule(jobs, key):  # order the jobs such that minimizing the max lateness
    jobs.sort(key=key)
    C = 0
    max_lateness = 0
    for p, d in jobs:
        C += p
        lateness = (0 if C <= d else (C - d))
        if lateness > max_lateness:
            max_lateness = lateness

    return max_lateness


def main():
    # with open('jobs.txt') as fhandle:
    #     jobs = []
    #     for line in fhandle:
    #         p, d = line.split()
    #         jobs.append((int(p), int(d)))
    jobs = data_generator()
    pj = lambda x: x[0]
    dj = lambda x: x[1]
    pd = lambda x: x[0] * x[1]
    print('increasing order of processing time: max_lateness = ', schedule(jobs, pj))
    print('increasing order of deadlines: max_lateness = ', schedule(jobs, dj))
    print('increasing order of the product pj & dj: max_lateness = ', schedule(jobs, pd))


if __name__ == '__main__':
    main()
