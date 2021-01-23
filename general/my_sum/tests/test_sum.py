# source: https://realpython.com/python-testing/

import unittest
from fractions import Fraction

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integres
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_tuple_float(self):
        data = [2.1, 2.5, 3.6]
        result = sum(data)
        self.assertEqual(result, 8.2)

    def test_list_fractions(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == "__main__":
    unittest.main()
