# -*- coding: utf-8 -*-

def main():
    a, b, x = map(int, input().split())
    print ('YES' if (x >= a and x <= a + b) else 'NO')

if __name__ == '__main__':
    main()
