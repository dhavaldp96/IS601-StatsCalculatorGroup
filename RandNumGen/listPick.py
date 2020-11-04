import random

class ListPick:

    #Select a random item from a list
    @staticmethod
    def listPick(data):
        return random.choice(data)

    #Set a seed and randomly.select the same value from a list
    @staticmethod
    def listPickSeed(seed, data):
        random.seed(seed)
        return ListPick.listPick(data)

    #Select N number of items from a list without a seed
    @staticmethod
    def listPickList(nums, data):
        temp = []
        while len(temp) < nums:
            temp.append(ListPick.listPick(data))
        return temp

    #Select N number of items from a list with a seed
    @staticmethod
    def listPickListSeed(seed, nums, data):
        random.seed(seed)
        return ListPick.listPickList(nums, data)