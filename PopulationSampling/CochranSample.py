"""


@Time    : 11/4/20
@Author  : Wenbo
"""

from DescriptiveStat.zsc import ZScore
from PopulationSampling.MarginOfError import MarginOfError
from DescriptiveStat.populationProportion import PopulationProportion
from Calculator.exponent import Exponent
from Calculator.sub import sub


class Cochran:
    @staticmethod
    def cochran(data, seeds, nums):
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        z = ZScore.zscore(seeds,data)
        pp = PopulationProportion.population_porportion(seeds, nums, data)
        MarOfError = MarginOfError.marginOfError(seeds, data)
        s = sub(pp, 1)
        cochran = (Exponent.power(z, 2) * pp * s) / Exponent.power(MarOfError, 2)
        return cochran