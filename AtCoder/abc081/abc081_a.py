# -*- coding: utf-8 -*-

def main():
    input_char_list = list(input())
    count = 0
    for char in input_char_list:
        if char == '1':
            count += 1
    print(count)

if __name__ == '__main__':
    main()
