import random

class RandNum:

    # Generating a random number without a seed between a range of two numbers
    # Integer
    @staticmethod
    def randNum(lower, upper):
        return random.randint(lower, upper)
    # And Decimal
    @staticmethod
    def randFloat(lower, upper):
        return random.uniform(lower, upper)

    # Generating a random number with a seed between a range of two numbers
    # Integer
    @staticmethod
    def randNumSeed(seed,lower,upper):
        random.seed(seed)
        return RandNum.randNum(lower,upper)

    # And Decimal
    @staticmethod
    def randFloatSeed(seed,lower,upper):
        random.seed(seed)
        return RandNum.randFloat(lower,upper)
