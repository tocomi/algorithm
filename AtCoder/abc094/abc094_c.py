# -*- coding: utf-8 -*-

import copy

def main():
    n = int(input())
    x = list(map(int, input().split()))

    t = copy.deepcopy(x)
    t.remove(min(x))
    t.sort()
    m1 = t[int(n / 2 - 1)]
    t = copy.deepcopy(x)
    t.remove(max(x))
    t.sort()
    m2 = t[int(n / 2 - 1)]
    for i in range(n):
        print(m1 if x[i] < m1 else m2)

if __name__ == '__main__':
    main()
