#!/usr/bin/python3
"""Below module is for unittests."""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Creates test class object."""
    def test_one(self):
        matrix1 = [0, 1, 2, 3, 4]
        self.assertEqual(max_integer(matrix1), 4)

    def test_two(self):
        matrix2 = []
        self.assertEqual(max_integer(matrix2), None)

    def test_three(self):
        self.assertRaises(TypeError, max_integer, 0)

    def test_four(self):
        matrix4 = {0: 'a', 1: 'b', 2: 'c'}
        self.assertRaises(KeyError, max_integer, matrix4)

    def test_five(self):
        matrix5 = ['a', 'b', 'c']
        self.assertEqual(max_integer(matrix5), 'c')

    def test_six(self):
        matrix6 = 'hello'
        self.assertEqual(max_integer(matrix6), 'o')


if __name__ == "__main__":
    unittest.main()
