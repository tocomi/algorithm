# -*- coding: utf-8 -*-

def main():
    a_500 = int(input())
    b_100 = int(input())
    c_50 = int(input())
    x = int(input())
    count = 0

    for a in range(a_500 + 1):
        if ((500 * a) > x):
            continue
        for b in range(b_100 + 1):
            if ((500 * a) > x):
                continue
            for c in range(c_50 + 1):
                if ((500 * a) > x):
                    continue
                if (((500 * a) + (100 * b) + (50 * c)) == x):
                    count += 1

    print(count)

if __name__ == '__main__':
    main()
