import numpy

class Mean:

    @staticmethod
    def mean(data):
        if len(data)==0:
            raise ValueError("data cannot be empty list")
        return numpy.mean(data)