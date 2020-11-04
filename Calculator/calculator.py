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

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = add(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = sub(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = mul(a, b)
        return self.result

    def divide(self, a, b):
        self.result = div(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def squareroot(self, a):
        self.result = square_root(a)
        return self.result