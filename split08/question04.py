import unittest


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
        return (p*(p - self.side1)*(p - self.side2)*(p - self.side3))**0.5


class TriangleTest(unittest.TestCase):

    def test_invalid_triangle(self):
        with self.assertRaises(TriangleNotExistException):
            Triangle([7, 7, 15])

    def test_invalid_arguments(self):
        with self.assertRaises(TriangleNotValidArgumentException):
            Triangle(['3', 4, 5])
            Triangle('string')
            Triangle([7, 2])

    def test_get_area(self):
        sides = [3, 2, 4]
        triangle = Triangle(sides)
        p = sum(sides) / 2
        triangle_area = (p * (p-sides[0]) * (p-sides[1]) * (p-sides[2]))**0.5
        self.assertEqual(triangle.get_area(), triangle_area)
