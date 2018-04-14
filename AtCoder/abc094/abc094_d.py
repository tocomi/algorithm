# -*- coding: utf-8 -*-

import math

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    a.remove(m)

    ans = m
    h = m / 2
    dif = 9999999999
    for num in a:
        if abs(h - num) < dif:
            ans = num
            dif = abs(h - num)

    print(m)
    print(ans)

if __name__ == '__main__':
    main()
