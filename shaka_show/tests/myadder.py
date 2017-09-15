"""
A class used as an example for learning how to test a class behavior
"""

class MyAdder:

    def __init__(self):
        self.numbers = []

    def pushNumber(self, number):
        self.numbers.append(number);

    def sum(self):
        return sum(self.numbers)

    def get(self):
        return
