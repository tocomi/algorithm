# -*- coding: utf-8 -*-

def main():
    args = input().split()
    a, b = int(args[0]) ,int(args[1])
    result = 'Even' if ( a * b ) % 2 == 0 else 'Odd'
    print(result)

if __name__ == '__main__':
    main()
