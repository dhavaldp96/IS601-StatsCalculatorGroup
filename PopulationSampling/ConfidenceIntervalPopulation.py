"""
Confidence Interval Population

@Time    : 11/4/20
@Author  : Wenbo
"""

from scipy.stats import sem
from scipy.stats import t
from DescriptiveStat.mean import Mean


class ConfidenceIntervalPopulation:

    @staticmethod
    def confidence_interval_population(confidence, data):
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        m = Mean.mean(data)
        stder = sem(data)
        h = stder * t.ppf((1 + confidence) / 2, len(data) - 1)
        beginInterval = m - h
        endInterval = m + h
        return beginInterval, endInterval