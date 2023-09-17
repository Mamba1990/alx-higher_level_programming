#!/usr/bin/python3

""" Represents the Base class"""
import json
import csv
import os.path


class Base:
    """ Defines the class Base.

    Private Class Attributes:
        __nb_object (int): The instantiated Bases'.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing the instances of the class Base.

        Args:
            id (int): The new Base's identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Defines list to JSON string

        Args:
            list_dictionaries (list): dictionaries'.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves the object in a file

        Args:
            list_objs (list): The inherited Base instances'.
        """
        filename = "{}.json".format(cls.__name__)
        listDic = []

        if not list_objs:
            pass
        else:
            for k in range(len(list_objs)):
                listDic.append(list_objs[k].to_dictionary())

        _lists = cls.to_json_string(listDic)

        with open(filename, 'w') as fi:
            fi.write(_lists)

    @staticmethod
    def from_json_string(json_string):
        """Deserializes JSON string to dictionary .

        Args:
            json_string (str): A JSON str representing of a dicts' list.
        Returns:
            json_string is None or empty - an empty list.
            Otherwise - list represented by json_string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairing of attributes
            to be initialized.
        """
        if cls.__name__ == "Rectangle":
            _new = cls(10, 10)
        else:
            _new = cls(10)
        _new.update(**dictionary)
        return _new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances a file of JSON strings.

        Returns:
            file doesn't exist - empty list.
            Otherwise - list of instantiated classes.
        """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as fi:
            listStr = fi.read()

        listCls = cls.from_json_string(listStr)
        listIns = []

        for idx in range(len(listCls)):
            listIns.append(cls.create(**listCls[idx]))

        return listIns

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves list of objects to  CSV file .

         Args:
            list_objs (list): The inherited Base instances' list.
        """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            listDic = [0, 0, 0, 0, 0]
            listKeys = ['id', 'width', 'height', 'x', 'y']
        else:
            listDic = ['0', '0', '0', '0']
            listKeys = ['id', 'size', 'x', 'y']

        mat = []

        if not list_objs:
            pass
        else:
            for ob in list_objs:
                for kv in range(len(listKeys)):
                    listDic[kv] = ob.to_dictionary()[listKeys[kv]]
                mat.append(listDic[:])

        with open(filename, 'w') as write_File:
            writer = csv.writer(write_File)
            writer.writerows(mat)

    @classmethod
    def load_from_file_csv(cls):
        """loads list of classes instantiated from a CSV file.

        Returns:
            the file doesn't exist - empty list.
            Otherwise - list of the instantiated classes.
        """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as read_File:
            _reader = csv.reader(read_File)
            csvList = list(_reader)

        if cls.__name__ == "Rectangle":
            listKeys = ['id', 'width', 'height', 'x', 'y']
        else:
            listKeys = ['id', 'size', 'x', 'y']

        mat = []

        for csv_el in csvList:
            dictCsv = {}
            for kv in enumerate(csv_el):
                dictCsv[listKeys[kv[0]]] = int(kv[1])
            mat.append(dictCsv)

        listIns = []

        for idx in range(len(mat)):
            listIns.append(cls.create(**mat[idx]))

        return listIns
