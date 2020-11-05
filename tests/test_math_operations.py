"""
Unit test for Addition

@Time    : 11/4/20
@Author  : Wenbo
"""

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../'))

import unittest

from Calculator.addition import Addition


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_sum_list(self):
        valuelist = [1, 2, 3]
        self.assertEqual(6, Addition.sum(valuelist))


if __name__ == '__main__':
    unittest.main()
