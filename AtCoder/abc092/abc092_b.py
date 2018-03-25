# -*- coding: utf-8 -*-

def main():
    n = int(input())
    d, x = map(int, input().split())

    c = 0
    for _ in range(n):
        a = int(input())
        for b in range(0,100):
            if a * b + 1 <= d:
                c += 1
            else:
                break

    print(c + x)

if __name__ == '__main__':
    main()
