import unittest
from mylibrary.math_func import my_sum

class TestMathFunc(unittest.TestCase):
    def my_sum_test(self):
        self.assertEqual(my_sum(2, 3), 5)
        self.assertAlmostEqual(my_sum(1.2, 3.4), 4.6)
