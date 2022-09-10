#! /usr/bin/env python3

from heapq import heappush, heappop
from heapq_max import heappush_max, heappop_max


def main():
    heap_sum = 0
    first, second, *other = [int(x) for x in open('Median.txt')]
    heap_sum += first
    if first > second:
        heap_low = [second]
        heap_high = [first]
        heap_sum += (heap_low[0])
    else:
        heap_low = [first]
        heap_high = [second]
        heap_sum += ([heap_low[0]])
    for number in other:
        if len(heap_low) % 2 == 0 and len(heap_high) % 2 == 0:
            if number > heap_low[0]:
                heappush(heap_high, number)
                temp = heappop(heap_high)
                heappush_max(heap_low, temp)
                heap_sum += (heap_low[0])
            else:
                heappush_max(heap_low, number)
                heap_sum += (heap_low[0])
        elif len(heap_low) % 2 != 0 and len(heap_high) % 2 != 0:
            if number > heap_low[0]:
                heappush(heap_high, number)
                temp = heappop(heap_high)
                heappush_max(heap_low, temp)
                heap_sum += (heap_low[0])
            else:
                heappush_max(heap_low, number)
                heap_sum += (heap_low[0])
        elif len(heap_low) - len(heap_high) == 1:
            if number > heap_low[0]:
                heappush(heap_high, number)
                heap_sum += (heap_low[0])
            else:
                heappush_max(heap_low, number)
                temp = heappop_max(heap_low)
                heappush(heap_high, temp)
                heap_sum += (heap_low[0])
        else:
            print(f'{heap_low} , {heap_high}')
            exit()
    assert (heap_sum % 10000 == 1213)


if __name__ == '__main__':
    main()
