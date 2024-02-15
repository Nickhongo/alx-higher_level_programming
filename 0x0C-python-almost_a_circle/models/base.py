#!/usr/bin/python3

import json
import csv
from pathlib import Path
import turtle
"""Base class"""


class Base:
    """Base class representation"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize Base Instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return Json string representation"""
        if isinstance(list_dictionaries, (list,)) or list_dictionaries is None:
            if type(list_dictionaries) is list:
                for _ in list_dictionaries:
                    if not isinstance(_, dict):
                        raise TypeError(
                            "list_dictionaries must be a list of dictionaries"
                        )
        else:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return list represented by json string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON str representation"""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            json_string = cls.to_json_string(
                    [obj.to_dictionary()for obj in list_objs])
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all the attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(10, 5)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = cls(10)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a json file
        """
        filename = cls.__name__ + ".json"
        path_to_file = Path(filename)

        if not path_to_file.exists():
            return []

        output = []
        with open(filename, "r") as file:
            instances = file.read()

            list_instances = cls.from_json_string(instances)
            for inst in list_instances:
                inst_details = cls.create(**inst)
                output.append(str(inst_details))
        return output

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes to a CSV file
        """
        if isinstance(list_objs, (list,)):
            for _ in list_objs:
                if not isinstance(_, Base):
                    raise TypeError(
                        "list_objs must be a list of instances that" +
                        " inherits from Base or None"
                    )
        else:
            raise TypeError(
                "list_objs must be a list of instances that" +
                " inherits from Base or None"
            )

        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
            with open(filename, "w") as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()

                obj_dictionaries = []
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    obj_dictionaries.append(obj_dict)
                for obj in obj_dictionaries:
                    writer.writerow(obj)

        elif cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]
            with open(filename, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()

                obj_dictionaries = []
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    obj_dictionaries.append(obj_dict)
                for obj in obj_dictionaries:
                    writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """
        Reads from a CSV file
        """

        filename = cls.__name__ + ".csv"

        path_to_file = Path(filename)

        if not path_to_file.exists():
            return []

        list_instances = []
        with open(filename, "r") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                if len(row) == 5:
                    list_instances.append("[{}] ({}) {}/{} - {}/{}".format(
                        "Rectangle",
                        row["id"],
                        row["x"],
                        row["y"],
                        row["width"],
                        row["height"]
                    ))
                elif len(row) == 4:
                    list_instances.append("[{}] ({}) {}/{} - {}".format(
                        "Square",
                        row["id"],
                        row["x"],
                        row["y"],
                        row["size"],
                    ))
        return list_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics module"""

        screen = turtle.Screen()
        t = turtle.Turtle()
        t.speed(1)

        for rect in list_rectangles:
            dictionary = rect.to_dictionary()
            x = dictionary["x"]
            y = dictionary["y"]
            width = dictionary["width"]
            height = dictionary["height"]

            t.penup()
            t.goto(x, y)
            t.pendown()
            t.color("blue")
            t.begin_fill()
            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)
            t.end_fill()

        for square in list_squares:
            dictionary = square.to_dictionary()
            x = dictionary["x"]
            y = dictionary["y"]
            size = dictionary["size"]

            t.penup()
            t.goto(x, y)
            t.pendown()
            t.color("red")
            t.begin_fill()
            for _ in range(4):
                t.forward(square.size)
                t.right(90)
            t.end_fill()

        screen.exitonclick()
