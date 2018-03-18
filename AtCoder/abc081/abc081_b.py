# -*- coding: utf-8 -*-

def devide_recursive(a, count):
    for number in a:
        if number % 2 != 0:
            return count
    count += 1
    return devide_recursive(list(map(lambda x: x / 2, a)), count)

def main():
    n = int(input())
    a = list(map(int, input().split()))

    print(devide_recursive(a, 0))

if __name__ == '__main__':
    main()
