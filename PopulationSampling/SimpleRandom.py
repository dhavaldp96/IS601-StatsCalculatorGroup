"""
Simple random sampling

@Time    : 11/4/20
@Author  : Wenbo
"""

import random
from RandNumGen.listPick import ListPick

class SimpleRandom:

    @staticmethod
    def simple_random_simpling(seed, nums, data):
        random.seed(seed)
        return ListPick.listPickListSeed(seed, nums, data)