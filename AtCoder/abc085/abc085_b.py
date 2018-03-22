# -*- coding: utf-8 -*-

def main():
    n = int(input())
    a = [ int(input()) for b in range(n)]

    print(len(set(a)))

if __name__ == '__main__':
    main()
