"""
Unit test for Calculator

@Time    : 11/4/20
@Author  : Wenbo
"""

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../'))

import unittest

from Calculator.calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.add(1, 2)
        self.assertEqual(3, result)

    def test_calculator_access_sum_result(self):
        self.calculator.add(1, 2)
        self.assertEqual(3, self.calculator.result)

    def test_calculator_return_difference(self):
        result = self.calculator.subtract(2, 1)
        self.assertEqual(-1, result)

    def test_calculator_access_difference_result(self):
        self.calculator.subtract(2, 1)
        self.assertEqual(-1, self.calculator.result)

    def test_calculator_return_product(self):
        result = self.calculator.multiply(1, 2)
        self.assertEqual(2, result)

    def test_calculator_access_product_result(self):
        self.calculator.multiply(1, 2)
        self.assertEqual(2, self.calculator.result)

    def test_calculator_divide(self):
        result = self.calculator.divide(5, 10)
        self.assertEqual(2, result)

    def test_calculator_root(self):
        result = self.calculator.squareroot(9)
        self.assertEqual(3, result)

    def test_calculator_power(self):
        result = self.calculator.square(4)
        self.assertEqual(16, result)


if __name__ == '__main__':
    unittest.main()