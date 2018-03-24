# -*- coding: utf-8 -*-

def is_contains_word(s, words):
    for word in words:
        if s == '':
            return True
        if s.endswith(word):
            return is_contains_word(s[:-len(word)], words)
    return False

def main():
    s = input()
    words = ('dream', 'dreamer', 'erase', 'eraser')

    print('YES') if is_contains_word(s, words) else print('NO')

if __name__ == '__main__':
    main()
