import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    """
    setUp function is called every time before a test function is ran.
    Anything that is made consistently should be put in here.
    For example, if we were to create Employee objects in every test but they can be
    the same, we can simply put them in setUp.
    """
    def setUp(self):
        self.employee1 = Employee('Penny', 'Worthshire', 20.00)
        self.employee2 = Employee('Alfred', 'Jackson', 18.50)


    """
    tearDown is code that is run every time after a test ends.
    """
    def tearDown(self):
        pass


    """
    Beginning of tests

    All tests are functions of the form test_*(self):.
    setUp is called before every test and tearDown is called after every test.
    """

    """
    Assert that unittest is functioning correctly.
    """
    def test_working(self):
        self.assertTrue(True)

    """
    Assert that member variables are setup correctly from setup
    """
    def test_init(self):
        self.assertEqual(self.employee1.first, 'Penny')
        self.assertEqual(self.employee1.last, 'Worthshire')
        self.assertEqual(self.employee1.pay, 20.00)
        self.assertEqual(self.employee2.first, 'Alfred')
        self.assertEqual(self.employee2.last, 'Jackson')
        self.assertEqual(self.employee2.pay, 18.50)

    def test_email(self):
        self.assertEqual(self.employee1.email(), 'penny.worthshire@company.com')
        self.assertEqual(self.employee2.email(), 'alfred.jackson@company.com')

    def test_next_check(self):
        self.assertEqual(self.employee1.nextCheck(), 3200)
        self.assertEqual(self.employee2.nextCheck(), 2960)

    def test_fullname(self):
        self.assertEqual(self.employee1.fullname(), 'Penny Worthshire')
        self.assertEqual(self.employee2.fullname(), 'Alfred Jackson')


if __name__ == '__main__':
    unittest.main()
