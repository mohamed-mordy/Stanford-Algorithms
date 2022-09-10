#!/usr/bin/env python3

import heapdict
from math import inf
import random

heap = heapdict.heapdict()
mymap = {1:'a', 2:'b'}
print(f'the random choice is:{random.choice(mymap)}')

heap['mohamed'] = 1
heap['mahmoud'] = inf
heap['ahmed'] = inf
heap['mohamed'] = -inf

while heap:
	print(heap.popitem())

