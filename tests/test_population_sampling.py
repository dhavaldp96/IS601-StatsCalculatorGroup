"""
Unit test for PopulationSampling

@Time    : 11/4/20
@Author  : Wenbo
"""

import sys
from os.path import abspath, join, dirname
sys.path.insert(0, join(abspath(dirname(__file__)), '../'))


import unittest
import random

from PopulationSampling.MarginOfError import MarginOfError
from PopulationSampling.ConfidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSampling.CochranSample import Cochran
from PopulationSampling.ConfidenceIntervalSample import ConfidenceIntervalSample
from PopulationSampling.FindSampleSize import UnknownPopulationStdev
from PopulationSampling.SimpleRandom import SimpleRandom


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1, 2, 3, 4, 5, 6]
        random.seed(1)

    def test_marginOfError(self):
        result = MarginOfError.marginOfError(2, self.test)
        self.assertEqual(result, -2.5)

    def test_confidenceIntervalPopulation(self):
        result = ConfidenceIntervalPopulation.confidence_interval_population(confidence=.90, data=self.test)
        self.assertEqual(result, (1.9609813838743337, 5.0390186161256665))

    def test_confidenceIntervalSample(self):
        result = ConfidenceIntervalSample.confidence_interval_sample(confidence=.90, seed=1, nums=5, data=self.test)
        self.assertEqual(result, (0.8046719486285641, 3.9953280513714358))

    def test_unknownPopulationStdev(self):
        result = UnknownPopulationStdev.unknownPopulationStdev(seed=1, data=self.test, percent=.50)
        self.assertEqual(result, 0.07142857142857144)

    def test_cochran(self):
        result = Cochran.cochran(data=self.test, seeds=1, nums=4)
        self.assertEqual(result,  0.0634920634920635)

    def test_simpRandSamp(self):
        result = SimpleRandom.simple_random_simpling(3,3, self.test)
        x = None
        for i in result:
            if i in self.test:
                x = True
            else:
                x = False
        self.assertEqual(True, x)


if __name__ == '__main__':
    unittest.main()
