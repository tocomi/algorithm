# -*- coding: utf-8 -*-

import unittest

import sys
import abc049_c as main

class TestMain(unittest.TestCase):

    def test_true(self):
        words = ('dream', 'dreamer', 'erase', 'eraser')
        input_word = 'dreamerase'
        expected = True
        actual = main.is_contains_word(input_word, words)
        self.assertEqual(expected, actual)

    def test_false(self):
        words = ('dream', 'dreamer', 'erase', 'eraser')
        input_word = 'dreamerasere'
        expected = False
        actual = main.is_contains_word(input_word, words)
        self.assertEqual(expected, actual)

    def test_duplicate_words_true(self):
        words = ('dream', 'dreamer', 'erase', 'eraser')
        input_word = 'dreamerdreamereraseerasedreamdreameraserdreameraser'
        expected = True
        actual = main.is_contains_word(input_word, words)
        self.assertEqual(expected, actual)

    def test_duplicate_words_false(self):
        words = ('dream', 'dreamer', 'erase', 'eraser')
        input_word = 'dredamerdredamerecraseecrasedrebamdreabmerasaerdreaameraser'
        expected = False
        actual = main.is_contains_word(input_word, words)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
