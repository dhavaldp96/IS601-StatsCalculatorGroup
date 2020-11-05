"""
Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation)

@Time    : 11/4/20
@Author  : Wenbo
"""

from Calculator.exponent import Exponent
from Calculator.div import div
from Calculator.sub import sub
from DescriptiveStat.zsc import ZScore
from PopulationSampling.MarginOfError import MarginOfError

class UnknownPopulationStdev:

    @staticmethod
    def unknownPopulationStdev(seed, data, percent):
        z = ZScore.zscore(seed, data)
        MarOfError = MarginOfError.marginOfError(seed, data)
        p = percent
        q = sub(p, 1)
        pq = div(MarOfError, z)
        samplePopulation = Exponent.power(pq, 2) * p * q
        return samplePopulation