#!/usr/bin/env python3

import sys
import threading

sys.setrecursionlimit(800000)
threading.stack_size(67108864)

""" start of user code"""
n = 0


def main():
    global n
    n += 1
    print(n)
    main()


if __name__ == '__main__':
    main()
""" end of user code"""

thread = threading.Thread(target=main)
thread.start()
