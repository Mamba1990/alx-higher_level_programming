#!/usr/bin/python3
""" Represents the tests for Rectangle class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Defines test for Rectangle class """

    def setUp(self):
        """ Invoked after each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """Defines tests for the new rectangle """
        _new = Rectangle(1, 1)
        self.assertEqual(_new.width, 1)
        self.assertEqual(_new.height, 1)
        self.assertEqual(_new.x, 0)
        self.assertEqual(_new.y, 0)
        self.assertEqual(_new.id, 1)

    def test_new_rectangle_2(self):
        """ Method tests new rectangle with all attrs """
        _new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(_new.width, 2)
        self.assertEqual(_new.height, 3)
        self.assertEqual(_new.x, 5)
        self.assertEqual(_new.y, 5)
        self.assertEqual(_new.id, 4)

    def test_new_rectangles(self):
        """Method Tests the new rectangles """
        _new = Rectangle(1, 1)
        new_2 = Rectangle(1, 1)
        self.assertEqual(False, _new is new_2)
        self.assertEqual(False, _new.id == new_2.id)

    def test_is_Base_instance(self):
        """Method Tests Rectangle is a Base instance """
        _new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(_new, Base))

    def test_incorrect_amount_attrs(self):
        """Method Tests error raise with o,e argument passed """
        with self.assertRaises(TypeError):
            _new = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        """Method tests error raised with no arguments passed """
        with self.assertRaises(TypeError):
            _new = Rectangle()

    def test_access_private_attrs(self):
        """Method allows to access to a private attribute """
        _new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            _new.__width

    def test_access_private_attrs_2(self):
        """ Method allows to access to a private attribute """
        _new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            _new.__height

    def test_access_private_attrs_3(self):
        """ Method allows to access to a private attribute """
        _new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            _new.__x

    def test_access_private_attrs_4(self):
        """ Method allows to access to a private attribute """
        _new = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            _new.__y

    def test_valide_attrs(self):
        """ Method allows to pass a string value """
        with self.assertRaises(TypeError):
            _new = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Method allows to pass a string value """
        with self.assertRaises(TypeError):
            _new = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        """Method allows to pass a string value """
        with self.assertRaises(TypeError):
            _new = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        """ Method allows to pass a string value """
        with self.assertRaises(TypeError):
            _new = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        """ Method  passing invalid values """
        with self.assertRaises(ValueError):
            _new = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """ Method  passing invalid values """
        with self.assertRaises(ValueError):
            _new = Rectangle(1, 0)

    def test_value_attrs_2(self):
        """ Method  passing invalid values """
        with self.assertRaises(ValueError):
            _new = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """ Method  passing invalid values """
        with self.assertRaises(ValueError):
            _new = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """Method Checks the return value of area. """
        _new = Rectangle(4, 5)
        self.assertEqual(_new.area(), 20)

    def test_area_2(self):
        """Method Checks the return value of area. """
        _new = Rectangle(2, 2)
        self.assertEqual(_new.area(), 4)
        _new.width = 5
        self.assertEqual(_new.area(), 10)
        _new.height = 5
        self.assertEqual(_new.area(), 25)

    def test_area_3(self):
        """Method Checks the return value of area. """
        _new = Rectangle(3, 8)
        self.assertEqual(_new.area(), 24)
        new_2 = Rectangle(10, 10)
        self.assertEqual(new_2.area(), 100)

    def test_display(self):
        """Method tests string displayed """
        rec = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Method tests string displayed """
        rec = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), res)

        rec.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Method tests__str__ return value """
        rec = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """Method tests __str__ return value """
        rec = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec)
            self.assertEqual(str_out.getvalue(), res)

        rec.id = 1
        rec.width = 7
        rec.height = 15
        res = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Method tests __str__ return value """
        rec = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec)
            self.assertEqual(str_out.getvalue(), res)

        rec = Rectangle(25, 86, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec)
            self.assertEqual(str_out.getvalue(), res)

        rec_1 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec_1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Test __str__ return value """
        rec = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(rec.__str__(), res)

    def test_display_3(self):
        """ Test __str__ return value """
        rec = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Test __str__ return value """
        rec = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), res)

        rec.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), res)

        rec.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """Method tests dictionary returned """
        rec = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(rec.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """Method tests dictionary returned """
        rec1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec1)
            self.assertEqual(str_out.getvalue(), res)

        rec2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec2)
            self.assertEqual(str_out.getvalue(), res)

        r1Dictionary = rec1.to_dictionary()
        rec2.update(**r1Dictionary)

        self.assertEqual(rec1.width, rec2.width)
        self.assertEqual(rec1.height, rec2.height)
        self.assertEqual(rec1.x, rec2.x)
        self.assertEqual(rec1.y, rec2.y)
        self.assertEqual(rec1.id, rec2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1Dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """Method  Tests Dictionary to JSON string """
        rec1 = Rectangle(2, 2)
        _dictionary = rec1.to_dictionary()
        json_dictionary = Base.to_json_string([_dictionary])
        res = "[{}]\n".format(_dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Method tets  arguments value passed """
        with self.assertRaises(ValueError):
            rec = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Method tests  arguments value passed"""
        with self.assertRaises(ValueError):
            rec = Rectangle(1, -2)

    def test_create(self):
        """ Method Tests creation."""
        _dictionary = {'id': 89}
        rec = Rectangle.create(**_dictionary)
        self.assertEqual(rec.id, 89)

    def test_create_2(self):
        """Method Tests creation. """
        _dictionary = {'id': 89, 'width': 1}
        rec = Rectangle.create(**_dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 1)

    def test_create_3(self):
        """ Method Tests creation. """
        _dictionary = {'id': 89, 'width': 1, 'height': 2}
        rec = Rectangle.create(**_dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)

    def test_create_4(self):
        """Method Tests creation. """
        _dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        rec = Rectangle.create(**_dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)

    def test_create_5(self):
        """Method Tests creation. """
        _dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        rec = Rectangle.create(**_dictionary)
        self.assertEqual(rec.id, 89)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)

    def test_load_from_file(self):
        """ Method Tests loading from file. """
        loadFile = Rectangle.load_from_file()
        self.assertEqual(loadFile, [])

    def test_load_from_file_2(self):
        """ Method Tests loading from file.  """
        rec1 = Rectangle(5, 5)
        rec2 = Rectangle(8, 2, 5, 5)

        lin_put = [rec1, rec2]
        Rectangle.save_to_file(lin_put)
        lout_put = Rectangle.load_from_file()

        for k in range(len(lin_put)):
            self.assertEqual(lin_put[k].__str__(), lout_put[k].__str__())
