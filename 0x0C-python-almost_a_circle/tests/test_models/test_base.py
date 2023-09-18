#!/usr/bin/python3
"""Import modules for tests."""
import unittest
import os.path
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for base class."""
    def test_id(self):
        """Tests for the id."""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_dictionary(self):
        """Tests for dictionaries."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertDictEqual(dictionary, {'id': 1, 'width': 10,
                                          'height': 7, 'x': 2, 'y': 8})
        json_dict = Base.to_json_string([dictionary])
        self.assertEqual(json_dict, json_dict)
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_save_file(self):
        """Tests for save file."""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Square(4)
        Rectangle.save_to_file([r1])
        Square.save_to_file([r2])
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(len(f.read()) > 1)
        with open("Square.json", 'r') as f:
            self.assertTrue(len(f.read()) > 1)

        Rectangle.save_to_file(None)
        Square.save_to_file(None)
        with open("Rectangle.json", 'r') as f:
            self.assertTrue(f.read() == "[]")
        with open("Square.json", 'r') as f:
            self.assertTrue(f.read() == "[]")

    def test_from_json(self):
        """Tests for json."""
        rectangle = [{'id': 89, 'width': 10, 'height': 4}]
        square = [{'id': 89, 'size': 4}]
        input_list = Rectangle.to_json_string(rectangle)
        output_list = Rectangle.from_json_string(input_list)
        self.assertTrue(type(output_list) is list)
        #output_list = Rectangle.from_json_string([])
        #self.assertTrue(output_list == [])
        output_list = Rectangle.from_json_string(None)
        self.assertTrue(output_list == [])
        input_list = Square.to_json_string(square)
        output_list = Square.from_json_string(input_list)
        self.assertTrue(type(output_list) is list)
        #output_list = Square.from_json_string([])
        #self.assertTrue(output_list == [])
        output_list = Square.from_json_string(None)
        self.assertTrue(output_list == [])

    def test_load(self):
        """Tests for file loading"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        r_input_list = [r1, r2]
        Rectangle.save_to_file(r_input_list)
        r_output_list = Rectangle.load_from_file()
        for x in r_output_list:
            self.assertTrue(type(x) is Rectangle)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        s_input_list = [s1, s2]
        Square.save_to_file(s_input_list)
        s_output_list = Square.load_from_file()
        for x in s_output_list:
            self.assertTrue(type(x) is Square)


if __name__ == "__main__":
    unittest.main()
