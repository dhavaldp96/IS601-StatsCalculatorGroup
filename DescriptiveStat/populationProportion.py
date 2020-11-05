"""
Population Proportion

@Time    : 11/4/20
@Author  : Wenbo
"""

from RandNumGen.listPick import ListPick

class PopulationProportion:

    @staticmethod
    def population_porportion(seeds, nums, data):
        p = ListPick.listPickListSeed(seeds, nums, data)
        pp = len(p) / len(data)
        return pp