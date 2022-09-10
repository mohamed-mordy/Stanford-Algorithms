#!/usr/bin/env python3

import collections

Job = collections.namedtuple('Job', ['weight', 'length'])


def min_weighted_sum(filename, key):
    with open(filename) as fhandle:
        fhandle.readline()
        jobs = []
        for line in fhandle:
            w, l = line.split()
            jobs.append(Job(int(w), int(l)))
        jobs.sort(key=lambda job_x: job_x.weight, reverse=True)
        jobs.sort(key=lambda job_x: key(job_x.weight, job_x.length), reverse=True)
        c = 0
        min_sum = 0
        for job in jobs:
            c += job.length
            min_sum += (job.weight * c)
    return min_sum


def main():
    difference = lambda x, y: x - y
    ratio = lambda x, y: x / y
    # print(min_weighted_sum('jobs_test2.txt', difference))  # 68615
    # print(min_weighted_sum('jobs_test1.txt', difference))  # 31
    print(min_weighted_sum('jobs.txt', difference))  # 69119377652
    # print(min_weighted_sum('jobs_test2.txt', ratio))  # 67247
    # print(min_weighted_sum('jobs_test1.txt', ratio))  # 29
    print(min_weighted_sum('jobs.txt', ratio))  # 67311454237


if __name__ == '__main__':
    main()
