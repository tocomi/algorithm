# -*- coding: utf-8 -*-

import unittest

import sys
import abc086_c as main

class TestMain(unittest.TestCase):

    def test_true(self):
        point = [[3, 1, 2], [6, 1, 1]]
        actual = main.can_reach(point)
        self.assertEqual(True, actual)

    def test_false(self):
        point = [[2, 1, 1], [3, 1, 1]]
        actual = main.can_reach(point)
        self.assertEqual(False, actual)

    def test_with_minus_false(self):
        point = [[2, 1, 1], [5, -3, -2]]
        actual = main.can_reach(point)
        self.assertEqual(False, actual)

if __name__ == '__main__':
    unittest.main()
