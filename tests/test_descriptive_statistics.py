"""
Unit tests

@Time    : 11/4/20
@Author  : Wenbo
"""

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../'))


import unittest
from random import random

from DescriptiveStat.mean import Mean
from DescriptiveStat.median import Median
from DescriptiveStat.mode import Mode
from DescriptiveStat.variance import Variance
from DescriptiveStat.stddev import Stddev
from DescriptiveStat.zsc import ZScore
from DescriptiveStat.populationProportion import PopulationProportion

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5]
        self.test1 = [1, 2, 2, 3, 4]
        self.test2 = [1, 2, 3]
        self.test3 = [1, 2, 3, 4, 5, 6, 7]
        self.test4 = [1, 2, 3, 4, 5, 6]
        self.test5 = [1, 2, 3, 3, 3, 4, 5]

    def test_Mean(self):
        self.assertEqual(3, Mean.mean(self.test))

    def test_mode(self):
        self.assertEqual(2, Mode.mode(self.test1))

    def test_median(self):
        self.assertEqual(2, Median.median(self.test2))

    def test_variance(self):
        self.assertEqual(2, Variance.variance(self.test))

    def test_stddev(self):
        self.assertEqual(1.5811388300841898, Stddev.stddev(self.test))

    def test_zsc(self):
        zsc = ZScore.zscore(1, self.test)
        self.assertEqual(zsc, -0.6324555320336759)

    def test_populationProportion(self):
        result = PopulationProportion.population_porportion(data=self.test1, nums=6, seeds=4)
        self.assertEqual(result, 1.2)


if __name__ == '__main__':
    unittest.main()
