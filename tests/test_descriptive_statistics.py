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

from RandNumGen.randList import RandList
import statistics

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5]
        self.test2 = [1, 2, 2, 3, 4]
        self.rand_test = RandList.randListFloat(length=6, seed=1, lower=1, upper=100)

    def test_Mean(self):
        self.assertEqual(round(statistics.mean(self.rand_test), 6), round(Mean.mean(self.rand_test),6) )
        self.rand_test = self.rand_test + RandList.randListFloat(length=3, seed=1, lower=1, upper=100)
        self.assertEqual(round(statistics.mean(self.rand_test), 6), round(Mean.mean(self.rand_test),6) )

    def test_mode(self):
        self.assertEqual(statistics.mode(self.rand_test), Mode.mode(self.rand_test))

    def test_median(self):
        self.assertEqual(statistics.median(self.rand_test), Median.median(self.rand_test))

    def test_variance(self):
        self.assertEqual(statistics.variance(self.rand_test), Variance.variance(self.rand_test))

    def test_stddev(self):
        self.assertEqual(statistics.stdev(self.rand_test), Stddev.stddev(self.rand_test))

    def test_zsc(self):
        zsc = ZScore.zscore(1, self.test)
        self.assertEqual(zsc, -0.6324555320336759)

    def test_populationProportion(self):
        result = PopulationProportion.population_porportion(data=self.test2, nums=6, seeds=4)
        self.assertEqual(result, 1.2)


if __name__ == '__main__':
    unittest.main()
