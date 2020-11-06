"""
Calculator

@Time    : 11/4/20
@Author  : Wenbo
"""


from Calculator.sub import sub
from Calculator.add import add
from Calculator.mul import mul
from Calculator.div import div
from Calculator.square import square
from Calculator.square_root import square_root
from HelperFunctions.helper import Helper

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        if not Helper.check_number(a) or not Helper.check_number(b):
            raise ValueError
        self.result = add(a, b)
        return self.result

    def subtract(self, a, b):
        if not Helper.check_number(a) or not Helper.check_number(b):
            raise ValueError
        self.result = sub(a, b)
        return self.result

    def multiply(self, a, b):
        if not Helper.check_number(a) or not Helper.check_number(b):
            raise ValueError
        self.result = mul(a, b)
        return self.result

    def divide(self, a, b):
        if not Helper.check_number(a) or not Helper.check_number(b):
            raise ValueError
        self.result = div(a, b)
        return self.result

    def square(self, a):
        if not Helper.check_number(a):
            raise ValueError
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        if not Helper.check_number(a):
            raise ValueError
        self.result = square_root(a)
        return self.result

if __name__ == '__main__':
    cal = Calculator()
    cal.add(1, "3")
    print(cal.result)
