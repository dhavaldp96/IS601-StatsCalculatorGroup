import numpy


class Variance:

    @staticmethod
    def variance(data):
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        return numpy.var(data)