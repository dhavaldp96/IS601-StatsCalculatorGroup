"""
Margin Of Error

@Time    : 11/4/20
@Author  : Wenbo
"""

from DescriptiveStat.stddev import Stddev
from DescriptiveStat.zsc import Zsc


class MarginOfError:
    @staticmethod
    def marginOfError(seed, data):
        zsc = Zsc.zsc(seed, data)
        stddev = Stddev.stddev(data)
        return zsc * stddev