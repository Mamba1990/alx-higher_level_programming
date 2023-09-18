#!/usr/bin/python3

"""Represents the  test Base class """
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ tests instantiation of the Base class """

    def setUp(self):
        """  Invokes for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Tests the assigned id """
        _new = Base(1)
        self.assertEqual(_new.id, 1)

    def test_id_default(self):
        """ Tests the default id """
        _new = Base()
        self.assertEqual(_new.id, 1)

    def test_id_nb_objects(self):
        """ Tests the  nb object attribute """
        _new = Base()
        new_2 = Base()
        new_3 = Base()
        self.assertEqual(_new.id, 1)
        self.assertEqual(new_2.id, 2)
        self.assertEqual(new_3.id, 3)

    def test_id_mix(self):
        """ Tests the nb object attributes and the assigned id """
        _new = Base()
        new_2 = Base(1024)
        new_3 = Base()
        self.assertEqual(_new.id, 1)
        self.assertEqual(new_2.id, 1024)
        self.assertEqual(new_3.id, 2)

    def test_string_id(self):
        """ Methos Test the string id """
        _new = Base('1')
        self.assertEqual(_new.id, '1')

    def test_more_args_id(self):
        """ Method Tests  passing more args to init method """
        with self.assertRaises(TypeError):
            _new = Base(1, 1)

    def test_access_private_attrs(self):
        """ Method tests the accessing to private attributes """
        _new = Base()
        with self.assertRaises(AttributeError):
            _new.__nb_objects

    def test_save_to_file_1(self):
        """ Method tests JSON file """
        Square.save_to_file(None)
        res = "[]\n"
        with open("Square.json", "r") as fi:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(fi.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as fi:
            self.assertEqual(fi.read(), "[]")

    def test_save_to_file_2(self):
        """Method tests JSON file """
        Rectangle.save_to_file(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as fi:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(fi.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as fi:
            self.assertEqual(fi.read(), "[]")
