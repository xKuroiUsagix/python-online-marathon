import unittest
from math import sqrt


class TriangleNotValidArgumentException(Exception):
    def __str__(self):
        return 'Not valid arguments'


class TriangleNotExistException(Exception):
    def __str__(self):
        return 'Can`t create triangle with this arguments'


class Triangle:
    def __init__(self, sides):
        self.__is_values_valid(sides)

        if (sides[0] < 0) or (sides[1] < 0) or (sides[2] < 0):
            raise TriangleNotExistException
        if (sides[0] + sides[1] <= sides[2]) or (sides[1] + sides[2] <= sides[0])\
                                             or (sides[2] + sides[0] <= sides[1]):
            raise TriangleNotExistException

        self.side1 = sides[0]
        self.side2 = sides[1]
        self.side3 = sides[2]

    @staticmethod
    def __is_values_valid(values):
        if not isinstance(values, (list, tuple)):
            raise TriangleNotValidArgumentException
        elif len(values) != 3:
            raise TriangleNotValidArgumentException

        for i in values:
            if isinstance(i, str):
                raise TriangleNotValidArgumentException

    def get_area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(p*(p - self.side1)*(p - self.side2)*(p - self.side3))


class TriangleTest(unittest.TestCase):
    def setUp(self):
        self.valid_test_data = [
            ((3, 4, 5), 6.0),
            ((10, 10, 10), 43.30),
            ((6, 7, 8), 20.33),
            ((7, 7, 7), 21.21),
            ((50, 50, 75), 1240.19),
            ((37, 43, 22), 406.99),
            ((26, 25, 3), 36.0),
            ((30, 29, 5), 72.0),
            ((87, 55, 34), 396.0),
            ((120, 109, 13), 396.0),
            ((123, 122, 5), 300.0)
        ]

        self.invalid_triangle = [
            (1, 2, 3),
            (1, 1, 2),
            (7, 7, 15),
            (100, 7, 90),
            (17, 18, 35),
            (127, 17, 33),
            (145, 166, 700),
            (1000, 2000, 1),
            (717, 17, 7),
            (0, 7, 7),
            (-7, 7, 7)
        ]

        self.invalid_arguments = [
            ('3', 4, 5),
            ('a', 2, 3),
            (7, "str", 7),
            ('1', '1', '1'),
            'string',
            (7, 2),
            (7, 7, 7, 7),
            'str',
            10,
            ('a', 'str', 7)
        ]

    def test_valid_triangle(self):
        for values, expected in self.valid_test_data:
            with self.subTest(query=values):
                self.assertAlmostEqual(Triangle(values).get_area(),
                                       expected,
                                       None,
                                       delta=0.01)

    def test_invalid_arguments(self):
        for values in self.invalid_arguments:
            with self.subTest(query=values):
                with self.assertRaises(TriangleNotValidArgumentException):
                    Triangle(values)

    def test_invalid_triangle(self):
        for values in self.invalid_triangle:
            with self.subTest(quesry=values):
                with self.assertRaises(TriangleNotExistException):
                    Triangle(values)
