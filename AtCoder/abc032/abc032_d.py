# -*- coding: utf-8 -*-

def main():

    N, W = map(int, input().split())
    v = [0] * N
    w = [0] * N
    m = {}

    for i in range(N):
        v[i], w[i] = map(int, input().split())

    def rec(i, j):
        res = 0
        if (i, j) in m:
            return m[(i, j)]
        if (i == N):
            return 0
        elif (j < w[i]):
            res = rec(i + 1, j)
        else:
            res = max(rec(i + 1, j), rec(i + 1, j - w[i]) + v[i])
        m[(i, j)] = res
        return res

    print(rec(0, W))

if __name__ == '__main__':
    main()
