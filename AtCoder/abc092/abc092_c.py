# -*- coding: utf-8 -*-

def main():
    n = int(input())
    a = list(map(int, input().split()))

    dis = 0
    bef = 0
    for b in a:
        dis += abs(bef - b)
        bef = b
    dis += abs(bef)
    for i in range(n):
        m = 0 if i == 0 else m = a[i-1]
        l = 0 if i == len(a) - 1 else l = a[i+1]
        print(dis - (abs(m - a[i]) + abs(a[i] - l) - abs(m - l)))

if __name__ == '__main__':
    main()
