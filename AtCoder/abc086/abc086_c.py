# -*- coding: utf-8 -*-

def can_reach(a):
    c = 0
    n = [0, 0]
    for point in a:
        c = point[0] - c
        dis = abs(point[1] - n[0]) + abs(point[2] - n[1])
        if (dis > c) or ((c - dis) % 2 != 0):
            return False
        c = point[0]
        n[0] = point[1]
        n[1] = point[2]
    return True

def main():
    n = int(input())
    a = [ list(map(int, input().split())) for _ in range(n)]

    print('Yes' if can_reach(a) else 'No')

if __name__ == '__main__':
    main()
