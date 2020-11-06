"""
Addition

@Time    : 11/4/20
@Author  : Wenbo
"""
from Calculator.calculator import Calculator

class Addition(Calculator):

    @staticmethod
    def sum(augend, addend=None):
        if isinstance(augend, list):
            return Addition.sumList(augend)
        return augend + addend

    @staticmethod
    def sumList(valueList):
        result = 0
        for value in valueList:
            result = Addition.sum(result, value)
        return result