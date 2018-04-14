# -*- coding: utf-8 -*-

def main():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(min(len([b for b in a if b < x]), len([b for b in a if b > x])))

if __name__ == '__main__':
    main()
