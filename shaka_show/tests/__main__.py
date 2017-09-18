'''
This allows you to run all tests in this test folder by typing python tests
from the shaka_show folder.
'''

import unittest

if __name__ == '__main__':
    all_tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(all_tests)
