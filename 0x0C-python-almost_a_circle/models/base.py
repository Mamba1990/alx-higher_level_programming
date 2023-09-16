#!/usr/bin/python3

"""Represents the base model class."""
import json
import csv
import turtle


class Base:
    """Base model class.

    This class represents the "base" for all other classes of the class.

    Private Class Attributes:
        __nb_object (int): the instantiated Bases' number.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new Base.

        Args:
            id (int): The new Base's identity.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionarieis):
        """returns the JSON string representation of dics list.

        Args:
            list_dictionaries (list): the dictionaries' list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of a list of objs to a file.

        Args:
            list_objs (list): the inherited Base instances's list.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                listDicts = [ob.to_dictionary() for ob in list_objs]
                json_file.write(Base.to_json_string(listDicts))

    @staticmethod
    def from_json_string(json_string):
        """Return list represented by list of dictionaries.

        Args:
            json_string (str): the JSON representation of a list of dicts.
        Returns:
            If json_string is None or empty - empty list.
            Otherwise - Python list of json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes set.

        Args:
            **dictionary (dict): the Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                _new = cls(1, 1)
            else:
                _new = cls(1)
            _new.update(**dictionary)
            return _new

    @classmethod
    def load_from_file(cls):
        """Returns the classes' list instantiated from a file of JSON str.

        Returns:
            file does not exist - an empty list.
            Otherwise - instantiated classes'.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                listDicts = Base.from_json_string(json_file.read())
                return [cls.create(**dc) for dc in listDicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV representation of a list of objs to a file.

        Args:
            list_objs (list): the inherited Base instances' list.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for ob in list_objs:
                    writer.writerow(ob.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return sa list of classes instantiated from  CSV file.

        Returns:
            file does not exist - an empty list.
            Otherwise -  instantiated classes' list.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                listDicts = csv.DictReader(csv_file, fieldnames=fieldnames)
                listDicts = [dict([j, int(v)] for j, v in dc.items())
                              for dc in listDicts]
                return [cls.create(**dc) for dc in listDicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares by using the turtle module.

        Args:
            list_rectangles (list): list of Rectangle objs to be drawn.
            list_squares (list): list of Square objs to be drawn.
        """
        turtl = turtle.Turtle()
        turtl.screen.bgcolor("#b7312c")
        turtl.pensize(3)
        turtl.shape("turtle")

        turtl.color("#ffffff")
        for rectg in list_rectangles:
            turtl.showturtle()
            turtl.up()
            turtl.goto(rectg.x, rectg.y)
            turtl.down()
            for i in range(2):
                turtl.forward(rectg.width)
                turtl.left(90)
                turtl.forward(rectg.height)
                turtl.left(90)
            turtl.hideturtle()

        turtl.color("#b5e3d8")
        for squ in list_squares:
            turtl.showturtle()
            turtl.up()
            turtl.goto(squ.x, squ.y)
            turtl.down()
            for j in range(2):
                turtl.forward(squ.width)
                turtl.left(90)
                turtl.forward(squ.height)
                turtl.left(90)
            turtl.hideturtle()

        turtle.exitonclick()
