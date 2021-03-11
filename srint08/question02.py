import unittest


def divide(num_1, num_2):
    return float(num_1) / num_2


class DivideTest(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_first_notnum(self):
        with self.assertRaises(ValueError):
            divide('string', 10)

    def test_second_notnum(self):
        with self.assertRaises(TypeError):
            divide(10, '10')

    def test_normal_division(self):
        self.assertEqual(divide(6, 3), 2)
