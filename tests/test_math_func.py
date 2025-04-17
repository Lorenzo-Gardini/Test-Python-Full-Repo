import unittest
from mylibrary.math_func import my_sum

class TestMathFunc(unittest.TestCase):
    def test_my_sum(self):
        self.assertEqual(my_sum(2, 3), 5)
        self.assertAlmostEqual(my_sum(1.2, 3.4), 4.6)
