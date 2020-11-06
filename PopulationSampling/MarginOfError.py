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
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        zsc = ZScore.zscore(seed, data)
        stddev = Stddev.stddev(data)
        return zsc * stddev