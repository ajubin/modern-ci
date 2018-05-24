import unittest
from model.factorial import factorial

class TestFactorialMethod(unittest.TestCase):

    def test_fact_0(self):
        self.assertEqual(factorial(0), 1)

    def test_fact_1(self):
        self.assertEqual(factorial(1), 1)

    def test_fact_10(self):
        self.assertEqual(factorial(10), 10*9*8*7*6*5*4*3*2*1)

    def test_invalid_n(self):
        with self.assertRaises(AssertionError):
            factorial('a')

if __name__ == '__main__':
    unittest.main()