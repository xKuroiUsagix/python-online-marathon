import unittest


def quadratic_equation(a, b, c):
    if a == b == c and a == 0:
        raise ValueError

    D = b**2 - 4*a*c
    if D < 0:
        return None
    elif not D:
        return (-b + D**0.5) / (2*a)

    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    return x1, x2


class QuadraticEquationTest(unittest.TestCase):
    def test_negative_discriminant(self):
        self.assertIsNone(quadratic_equation(5, 2, 1))

    def test_positive_discriminant(self):
        self.assertTupleEqual(quadratic_equation(1, 3, 2), (-1, -2))

    def test_zero_discriminant(self):
        self.assertEqual(quadratic_equation(1, 2, 1), -1)

    def test_wrong_value(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 0, 0)
