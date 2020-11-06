from RandNumGen.randNum import RandNum

class RandList:
# Generate a list of N random numbers with a seed and between a range of numbers

    # integer
    @staticmethod
    def randList(length, seed, lower, upper):
        data = []
        while len(data) < length:
            data.append(RandNum.randNumSeed(seed, lower, upper))
        return data

    # float
    @staticmethod
    def randListFloat(length, seed, lower,upper):
        data = []
        while len(data) < length:
            data.append(RandNum.randFloatSeed(seed, lower, upper))
        return data