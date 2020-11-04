"""
ZSC

@Time    : 11/4/20
@Author  : Wenbo
"""

from DiscriptiveStat.mean import Mean
from DiscriptiveStat.stddev import Stddev
from RandNumGen.listPick import ListPick

class Zsc:
    @staticmethod
    def zsc(seed, data):
        X = ListPick.listPickSeed(seed, data)
        mean = Mean.mean(data)
        stddev = Stddev.stddev(data)
        return (X - mean) / stddev