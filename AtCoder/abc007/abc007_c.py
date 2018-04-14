# -*- coding: utf-8 -*-

def main():

    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    c = [ list(input()) for _ in range(R)]
    g = []

    def print_maze(c):
        for a in c:
            print(','.join(list(map(str, a))).replace(',', ''))

    def rec(y, x, cnt):
        c[y][x] = cnt
        if y == gy - 1 and x == gx - 1:
            g.append(cnt)
        if c[y + 1][x] == '.' or (isinstance(c[y + 1][x], int) and c[y + 1][x] >= cnt):
            rec(y + 1, x, cnt + 1)
        if c[y][x + 1] == '.' or (isinstance(c[y][x + 1], int) and c[y][x + 1] >= cnt):
            rec(y, x + 1, cnt + 1)
        if c[y - 1][x] == '.' or (isinstance(c[y - 1][x], int) and c[y - 1][x] >= cnt):
            rec(y - 1, x, cnt + 1)
        if c[y][x - 1] == '.' or (isinstance(c[y][x - 1], int) and c[y][x - 1] >= cnt):
            rec(y, x - 1, cnt + 1)

    rec(sy - 1, sx - 1, 0)
    print(min(g))

if __name__ == '__main__':
    main()
