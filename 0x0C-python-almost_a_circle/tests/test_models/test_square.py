#!/usr/bin/python3
""" Represents the test Square class """
import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareMethods(unittest.TestCase):
    """ Method to test Square class """

    def setUp(self):
        """Invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_square(self):
        """ Method tests the new square """
        _new = Square(3)
        self.assertEqual(_new.size, 3)
        self.assertEqual(_new.width, 3)
        self.assertEqual(_new.height, 3)
        self.assertEqual(_new.x, 0)
        self.assertEqual(_new.y, 0)
        self.assertEqual(_new.id, 1)

    def test_new_square_2(self):
        """ Method tests the new square with all attrs """
        _new = Square(2, 5, 5, 4)
        self.assertEqual(_new.size, 2)
        self.assertEqual(_new.width, 2)
        self.assertEqual(_new.height, 2)
        self.assertEqual(_new.x, 5)
        self.assertEqual(_new.y, 5)
        self.assertEqual(_new.id, 4)

    def test_new_squares(self):
        """ Method tests new squares """
        _new = Square(1, 1)
        new_2 = Square(1, 1)
        self.assertEqual(False, _new is new_2)
        self.assertEqual(False, _new.id == new_2.id)

    def test_is_Base_instance(self):
        """ Method tests Square is a Base instance """
        _new = Square(1)
        self.assertEqual(True, isinstance(_new, Base))

    def test_is_Rectangle_instance(self):
        """Mrthod tests Square is a Rectangle instance """
        _new = Square(1)
        self.assertEqual(True, isinstance(_new, Rectangle))

    def test_incorrect_amount_attrs(self):
        """Method tests error raise with no args passed """
        with self.assertRaises(TypeError):
            _new = Square()

    def test_incorrect_amount_attrs_1(self):
        """method tests error raised with no args passed """
        with self.assertRaises(TypeError):
            _new = Square(1, 1, 1, 1, 1)

    def test_access_private_attrs(self):
        """ Method allows to access to a private attribute """
        _new = Square(1)
        with self.assertRaises(AttributeError):
            _new.__width

    def test_access_private_attrs_2(self):
        """ Method allows to access to a private attribute """
        _new = Square(1)
        with self.assertRaises(AttributeError):
            _new.__height

    def test_access_private_attrs_3(self):
        """ Method allows to access to a private attribute """
        _new = Square(1)
        with self.assertRaises(AttributeError):
            _new.__x

    def test_access_private_attrs_4(self):
        """ Method allows to access to a private attribute """
        _new = Square(1)
        with self.assertRaises(AttributeError):
            _new.__y

    def test_valide_attrs(self):
        """ Method to pass a string value"""
        with self.assertRaises(TypeError):
            _new = Square("2", 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Method to pass a string value """
        with self.assertRaises(TypeError):
            _new = Square(2, "2", 2, 2)

    def test_valide_attrs_3(self):
        """ Method to pass a string value """
        with self.assertRaises(TypeError):
            _new = Square(2, 2, "2", 2)

    def test_value_attrs(self):
        """ Method to pass invalid values """
        with self.assertRaises(ValueError):
           _new = Square(0)

    def test_value_attrs_2(self):
        """ Method to pass invalid values """
        with self.assertRaises(ValueError):
            _new = Square(1, -1)

    def test_value_attrs_3(self):
        """ Method to pass invalid values """
        with self.assertRaises(ValueError):
            _new = Square(1, 1, -1)

    def test_area(self):
        """Methods Checks the return value of area method """
        _new = Square(4)
        self.assertEqual(_new.area(), 16)

    def test_load_from_file(self):
        """Method test load from JSON file """
        loadFile = Square.load_from_file()
        self.assertEqual(loadFile, loadFile)

    def test_area_2(self):
        """Methods Checks the return value of area method """
        _new = Square(2)
        self.assertEqual(_new.area(), 4)
        _new.size = 5
        self.assertEqual(_new.area(), 25)

    def test_display(self):
        """ Method tests the string displayed """
        rec1 = Square(2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Method tests the string displayed"""
        rec1 = Square(4)
        res = "####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec1.display()
            self.assertEqual(str_out.getvalue(), res)

        rec1.size = 5
        res = "#####\n#####\n#####\n#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rec1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """Method tests __str__ return value """
        rec1 = Square(4, 2, 2)
        res = "[Square] (1) 2/2 - 4\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Method tests __str__ return value """
        rec1 = Square(3, 2, 5, 3)
        res = "[Square] (3) 2/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec1)
            self.assertEqual(str_out.getvalue(), res)

        rec1.id = 1
        rec1.size = 11
        res = "[Square] (1) 2/5 - 11\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rec1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """Method tests __str__ return value  """
        sq1 = Square(5)
        res = "[Square] (1) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

        sq2 = Square(3, 7, 1)
        res = "[Square] (2) 7/1 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq2)
            self.assertEqual(str_out.getvalue(), res)

        sq3 = Square(1, 1, 1)
        res = "[Square] (3) 1/1 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Method tests __str__ return value  """
        sq1 = Square(3)
        res = "[Square] (1) 0/0 - 3"
        self.assertEqual(sq1.__str__(), res)

    def test_display_3(self):
        """Method tests string displayed """
        sq1 = Square(5, 2, 1)
        res = "\n  #####\n  #####\n  #####\n  #####\n  #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            sq1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Method tests string displayed """
        sq1 = Square(3)
        res = "###\n###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            sq1.display()
            self.assertEqual(str_out.getvalue(), res)

        sq1.x = 1
        res = " ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            sq1.display()
            self.assertEqual(str_out.getvalue(), res)

        sq1.y = 2
        res = "\n\n ###\n ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            sq1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_update(self):
        """Method tests update method """
        sq1 = Square(3)
        res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

        sq1.update(5)
        _res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), _res)

    def test_update_2(self):
        """ Method tests update method """
        sq1 = Square(3)
        _res = "[Square] (1) 0/0 - 3\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), _res)

        sq1.update(5)
        res = "[Square] (5) 0/0 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_3(self):
        """ Method tests update method"""
        sq1 = Square(1)
        res = "[Square] (1) 0/0 - 1\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

        sq1.update(2, 2, 2, 2)
        res = "[Square] (2) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

        sq1.update(y=3)
        res = "[Square] (2) 2/3 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

        sq1.update(id=1, size=10)
        res = "[Square] (1) 2/3 - 10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_4(self):
        """ Method tests update method"""
        sq1 = Square(10)
        res = "[Square] (1) 0/0 - 10\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

        _dic = {'size': 3, 'y': 5}
        sq1.update(**_dic)
        res = "[Square] (1) 0/5 - 3\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

    def test_update_5(self):
        """ Method tests update method """
        sq1 = Square(7)
        res = "[Square] (1) 0/0 - 7\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), res)

        _dic = {'id': 10, 'x': '5', 'y': 5}

        with self.assertRaises(TypeError):
            sq1.update(**_dic)

    def test_to_dictionary(self):
        """ Methods tests to  dictionary returned """
        sq1 = Square(1, 2, 3)
        _res = "[Square] (1) 2/3 - 1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), _res)

        self.assertEqual(sq1.size, 1)
        self.assertEqual(sq1.width, 1)
        self.assertEqual(sq1.height, 1)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq1.y, 3)
        self.assertEqual(sq1.id, 1)

        _res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(sq1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), _res)

    def test_to_dictionary_2(self):
        """Methods tests to  dictionary returned """
        sq1 = Square(2, 2, 2)
        _res = "[Square] (1) 2/2 - 2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq1)
            self.assertEqual(str_out.getvalue(), _res)

        sq2 = Square(5)
        _res = "[Square] (2) 0/0 - 5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(sq2)
            self.assertEqual(str_out.getvalue(), _res)

        s1Dictionary = sq1.to_dictionary()
        sq2.update(**s1Dictionary)

        self.assertEqual(sq1.width, sq2.width)
        self.assertEqual(sq1.height, sq2.height)
        self.assertEqual(sq1.x, sq2.x)
        self.assertEqual(sq1.y, sq2.y)
        self.assertEqual(sq1.id, sq2.id)

        _res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(s1Dictionary))
            self.assertEqual(str_out.getvalue(), _res)

    def test_dict_to_json(self):
        """Method tests Dictionary to JSON string """
        sq1 = Square(2)
        _dictionary = sq1.to_dictionary()
        jsonDictionary = Base.to_json_string([_dictionary])
        _res = "[{}]\n".format(_dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(jsonDictionary)
            self.assertEqual(str_out.getvalue(), _res.replace("'", "\""))

    def test_json_file(self):
        """Method tests Dictionary to JSON string """
        sq1 = Square(2)
        _dictionary = sq1.to_dictionary()
        jsonDictionary = Base.to_json_string([_dictionary])
        _res = "[{}]\n".format(_dictionary.__str__())
        _res = _res.replace("'", "\"")

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(jsonDictionary)
            self.assertEqual(str_out.getvalue(), _res)

        Square.save_to_file([sq1])
        _res = "[{}]".format(_dictionary.__str__())
        _res = _res.replace("'", "\"")

        with open("Square.json", "r") as fi:
            _res2 = fi.read()

        self.assertEqual(_res, _res2)

    def test_value_square(self):
        """Method tests value pased to Square """
        with self.assertRaises(ValueError):
            sq1 = Square(-1)

    def test_create(self):
        """ The create method """
        _dictionary = {'id': 89}
        sq1 = Square.create(**_dictionary)
        self.assertEqual(sq1.id, 89)

    def test_create_2(self):
        """The create method """
        _dictionary = {'id': 89, 'size': 1}
        sq1 = Rectangle.create(**_dictionary)
        self.assertEqual(sq1.id, 89)
        self.assertEqual(sq1.size, 1)

    def test_create_3(self):
        """ The create method """
        _dictionary = {'id': 89, 'size': 1, 'x': 2}
        sq1 = Rectangle.create(**_dictionary)
        self.assertEqual(sq1.id, 89)
        self.assertEqual(sq1.size, 1)
        self.assertEqual(sq1.x, 2)

    def test_create_4(self):
        """The create method """
        _dictionary = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        sq1 = Rectangle.create(**_dictionary)
        self.assertEqual(sq1.id, 89)
        self.assertEqual(sq1.size, 1)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq1.y, 3)

    def test_load_from_file_2(self):
        """Method tests load from  JSON file """
        sq1 = Square(5)
        sq2 = Square(8, 2, 5)

        lin_put = [sq1, sq2]
        Square.save_to_file(lin_put)
        lout_put = Square.load_from_file()

        for k in range(len(lin_put)):
            self.assertEqual(lin_put[k].__str__(), lout_put[k].__str__())
