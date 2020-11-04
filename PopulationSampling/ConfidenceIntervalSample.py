"""
Confidence Interval Sample

@Time    : 11/4/20
@Author  : Wenbo
"""

from PopulationSampling.ConfidenceIntervalPopulation import ConfidenceIntervalPopulation
from PopulationSampling.SimpleRandom import SimpleRandom


class ConfidenceIntervalSample:

    @staticmethod
    def confidence_interval_sample(confidence, seed, nums, data):
        samp = SimpleRandom.simple_random_simpling(seed, nums, data)
        return ConfidenceIntervalPopulation.confidence_interval_population(confidence, samp)