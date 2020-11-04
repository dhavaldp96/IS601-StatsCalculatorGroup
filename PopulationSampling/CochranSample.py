"""


@Time    : 11/4/20
@Author  : Wenbo
"""

from DiscriptiveStat.zsc import ZScore
from PopulationSampling.MarginOfError import MarginOfError
from DiscriptiveStat.populationProportion import PopulationProportion
from Calculator.exponent import Exponent
from Calculator.sub import sub


class Cochran:
    @staticmethod
    def cochran(data, seeds, nums):
        z = ZScore.zscore(seeds,data)
        pp = PopulationProportion.population_porportion(seeds, nums, data)
        MarOfError = MarginOfError.marginOfError(seeds, data)
        s = sub(1, pp)
        cochran = (Exponent.power(z, 2) * pp * s) / Exponent.power(MarOfError, 2)
        return cochran