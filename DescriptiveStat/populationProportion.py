"""
Population Proportion

@Time    : 11/4/20
@Author  : Wenbo
"""

from RandNumGen.listPick import ListPick

class PopulationProportion:

    @staticmethod
    def population_porportion(seeds, nums, data):
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        p = ListPick.listPickListSeed(seeds, nums, data)
        pp = len(p) / len(data)
        return pp