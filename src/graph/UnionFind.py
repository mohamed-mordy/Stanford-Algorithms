#!/usr/bin/env python3

def ackermann(k, r):
    assert r >= 1
    if k == 0:
        return r + 1
    n_times = r
    result = r
    while n_times:
        result = ackermann(k-1, result)
        n_times -= 1
    return result


def inverseAckermann(n):
    t = 0
    while ackermann(t, 2) < n:
        t += 1
    return t


def test_ackermann():
    print(inverseAckermann(2048))
    print(ackermann(1, 2))
    print(ackermann(2, 2))
    print(ackermann(3, 2))


class UnionFind:
    def __init__(self):
        self.leaders = {}
        self.ranks = {}
        self.n_sets = 0
        pass

    def xfind(self, obj):
        if obj in self.leaders:
            tmp = obj
            leader = self.leaders[tmp]
            while leader != tmp:
                tmp = leader
                leader = self.leaders[tmp]
            return leader
        return None

    def find(self, obj):
        if obj not in self.leaders:
            self.leaders[obj] = obj
            self.ranks[obj] = 0
            self.n_sets += 1
            return obj
        else:
            tmp = obj
            leader = self.leaders[tmp]
            while leader != tmp:
                tmp = leader
                leader = self.leaders[tmp]
            self.leaders[obj] = leader
            return leader

    def union(self, obj1, obj2):
        l1 = self.find(obj1)
        l2 = self.find(obj2)
        if l1 == l2:
            return
        elif self.ranks[l1] == self.ranks[l2]:
            self.leaders[l2] = l1
            self.ranks[l1] += 1
        elif self.ranks[l1] > self.ranks[l2]:
            self.leaders[l2] = l1
        else:
            self.leaders[l1] = l2
        self.n_sets -= 1

    def print(self):
        print(f'the leaders map is: {self.leaders}')
        print(f'the ranks map is: {self.ranks}')


def test_unionfind():
    uf = UnionFind()
    print('invoking union(1, 2)')
    uf.union(1, 2)
    uf.print()
    print('invoking find(3)')
    uf.find(3)
    uf.print()
    print('invoking find(4) & find(5)')
    uf.find(4)
    uf.find(5)
    uf.print()
    print('invoking union(4, 5)')
    uf.union(4, 5)
    uf.print()
    print('invoking union(1, 5)')
    uf.union(1, 5)
    uf.print()
    print('invoking find(5)')
    uf.find(5)
    uf.print()


def main():
    test_unionfind()
    pass


if __name__ == '__main__':
    main()
