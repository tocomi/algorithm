# -*- coding: utf-8 -*-

def main():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort(reverse = True)
    ans = 0
    for i, num in enumerate(a):
        if i % 2 == 0:
            ans += num
        else:
            ans -= num

    print(ans)

if __name__ == '__main__':
    main()
