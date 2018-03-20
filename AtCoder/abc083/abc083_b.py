# -*- coding: utf-8 -*-

def main():
    n, a, b = map(int, input().split())
    total = 0

    for num in range(1, n + 1):
        chars = list(str(num))
        tmp = 0
        for char in chars:
            tmp += int(char)
        if a <= tmp and tmp <= b:
            total += num

    print(total)

if __name__ == '__main__':
    main()
