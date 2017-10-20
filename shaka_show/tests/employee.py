
class Employee:
    """
    Class to model properties an employee has.
    """

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def email(self):
        return '{}.{}@company.com'.format(self.first.lower(), self.last.lower())

    def next_check(self):
        return self.pay * 40 * 4

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
