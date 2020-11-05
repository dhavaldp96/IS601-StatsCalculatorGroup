"""
Z-score

@Time    : 11/4/20
@Author  : Wenbo
"""

from DescriptiveStat.mean import Mean
from DescriptiveStat.stddev import Stddev
from RandNumGen.listPick import ListPick

class ZScore:
    @staticmethod
    def zscore(seed, data):
        X = ListPick.listPickSeed(seed, data)
        mean = Mean.mean(data)
        stddev = Stddev.stddev(data)
        return (X - mean) / stddev