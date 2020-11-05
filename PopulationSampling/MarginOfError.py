"""
Margin Of Error

@Time    : 11/4/20
@Author  : Wenbo
"""

from DescriptiveStat.stddev import Stddev
from DescriptiveStat.zsc import ZScore


class MarginOfError:
    @staticmethod
    def marginOfError(seed, data):
        zsc = ZScore.zscore(seed, data)
        stddev = Stddev.stddev(data)
        return zsc * stddev