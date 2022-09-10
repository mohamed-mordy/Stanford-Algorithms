#!/usr/bin/env python3

class Heap:
    def __init__(self, *args):
        if args is None:
            self._heap = []
        else:
            self._heap = list(args)

    def __len__(self):
        return len(self._heap)

    def __repr__(self):
        return str(self._heap)

    def __getitem__(self, key):
        if len(self) >= key >= 1:
            return self._heap[key-1]
        else:
            raise IndexError("Illegal Heap Access. i.e., IndexError")

    def __setitem__(self, key, value):
        if len(self) >= key >= 1:
            self._heap[key-1] = value
        else:
            raise IndexError

    def __delitem__(self, key):
        if len(self) >= key >= 1:
            del self._heap[key-1]
        else:
            raise IndexError

    def push(self, value):
        self._heap.append(value)
        child = len(self)
        parent = child//2
        while self[parent] > self[child]:
            self[parent], self[child] = self[child], self[parent]
            child = parent
            parent = child//2 if child//2 else 1
        return self[1]

    def pop(self):
        min_value = self[1]
        self[1] = self[len(self)]
        del self[len(self)]
        parent = 1
        child1 = parent * 2
        child2 = parent * 2 + 1
        while self[parent] > self[child1] or self[parent] > self[child2]:
            if self[child1] < self[child2]:
                self[parent], self[child1] = self[child1], self[parent]
                parent = child1
            else:
                self[parent], self[child2] = self[child2], self[parent]
                parent = child2
            child1 = parent * 2
            child2 = parent * 2 + 1
            if child1 > len(self) and child2 > len(self):
                break
            elif self[parent] < self[child1]:
                self[parent], self[child1] = self[child1], self[parent]
                break
        return min_value

    def heapify(self):
        # TODO
        pass


heap = Heap(4, 4, 8, 9, 4, 12, 9, 11, 13)
print(heap)
print(heap.pop())
print(heap)
