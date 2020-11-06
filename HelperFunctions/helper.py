"""
Helper functions

@Time    : 11/6/20
@Author  : Wenbo
"""

class Helper():

    @staticmethod
    def check_float(a):
        return type(a) == float

    @staticmethod
    def check_int(a):
        return type(a) == int

    @staticmethod
    def check_number(a):
        return type(a) == float or type(a) == int


if __name__ == '__main__':
    print(Helper.check_float(1.11))
    print(Helper.check_float(1))
    print(Helper.check_float("1.11"))

    print(Helper.check_int(1.11))
    print(Helper.check_int(1))
    print(Helper.check_int("1.11"))

    print(Helper.check_number(1.11))
    print(Helper.check_number(1))
    print(Helper.check_number("1.11"))
