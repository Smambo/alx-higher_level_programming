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
        matrix4 = {5: 'a', 4: 'b', 3: 'c'}
        self.assertRaises(KeyError, max_integer, matrix4)

    def test_five(self):
        matrix5 = ['a', 'b', 'c']
        self.assertEqual(max_integer(matrix5), 'c')

    def test_six(self):
        matrix6 = 'hello'
        self.assertEqual(max_integer(matrix6), 'o')

    def test_seven(self):
        matrix7 = [-10, 1, 2, 3, 4]
        self.assertEqual(max_integer(matrix7), 4)

    def test_eight(self):
        matrix8 = [3]
        self.assertEqual(max_integer(matrix8), 3)

    def test_nine(self):
        matrix9 = [5, 1, 2, 3, 4]
        self.assertEqual(max_integer(matrix9), 5)

    def test_ten(self):
        matrix10 = [0, 1, 2, 7, 4]
        self.assertEqual(max_integer(matrix10), 7)


if __name__ == "__main__":
    unittest.main()
