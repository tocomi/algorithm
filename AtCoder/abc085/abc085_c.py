# -*- coding: utf-8 -*-

def main():
    n, y = map(int, input().split())

    for a in range(n + 1):
        if (a * 10000 > y):
            continue
        for b in range((n + 1) - a):
            c = n - (a + b)
            if ((a * 10000 + b * 5000 + c * 1000) == y):
                print('{} {} {}'.format(a, b, c))
                exit()

    print(-1, -1, -1)

if __name__ == '__main__':
    main()
