#!/usr/bin/python3
"""Import modules for tests."""
import unittest
import sys
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Tests for rectangle case."""

    def test_id(self):
        """Tests ids."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        r3.id = "d"
        self.assertEqual(r3.id, "d")

    def test_attr_errors(self):
        """Tests for exception errors."""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r1 = Rectangle(10, "3")
        with self.assertRaises(ValueError, msg="height must be > 0"):
            r1 = Rectangle(-5, 3)
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r1 = Rectangle({1: 3}, 2)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            r2 = Rectangle(10, 2)
            r2.width = -10
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r3 = Rectangle(10, 2)
            r3.x = {}
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            r4 = Rectangle(10, 2, 3, -1)

    def test_areas(self):
        """Tests areas."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r1 = Rectangle(2, 20)
        self.assertEqual(r1.area(), 40)

        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)

    def test_display(self):
        """Tests display."""
        Base._Base__nb_objects = 0
        old_stdout = sys.stdout
        sys.stdout = mystdout = StringIO()
        r1 = Rectangle(4, 2)
        r1.display()
        sys.stdout = old_stdout
        self.assertEqual(mystdout.getvalue(), "####\n####\n")
        sys.stdout = mystdout = StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        self.assertEqual(mystdout.getvalue(), "\n\n ##\n ##\n ##\n")
        sys.stdout = old_stdout

    def test_str(self):
        """Tests strings."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 1/0 - 5/5")
        r1 = Rectangle(1, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 0/0 - 1/1")


if __name__ == "__main__":
    unittest.main()
