import unittest


class Worker:

    def __init__(self, name, salary=0.0) -> None:
        if salary < 0:
            raise ValueError
        self.salary = salary
        self.name = name

    def __progressive_tax(self, salary_step):
        if 1001 <= salary_step <= 3000:
            return 0.1 * (3000 - 1000)
        elif 3001 <= salary_step <= 5000:
            return 0.15 * (5000 - 3000) + self.__progressive_tax(3000)
        elif 5001 <= salary_step <= 10000:
            return 0.21 * (10000 - 5000) + self.__progressive_tax(5000)
        elif 10001 <= salary_step <= 20000:
            return 0.3 * (20000 - 10000) + self.__progressive_tax(10000)
        elif 20001 <= salary_step <= 50000:
            return 0.4 * (50000 - 20000) + self.__progressive_tax(20000)
        else:
            return 0.0

    def get_tax_value(self):
        if 1001 <= self.salary <= 3000:
            return 0.1 * (self.salary - 1000)
        elif 3001 <= self.salary <= 5000:
            return 0.15 * (self.salary - 3000) + self.__progressive_tax(3000)
        elif 5001 <= self.salary <= 10000:
            return 0.21 * (self.salary - 5000) + self.__progressive_tax(5000)
        elif 10001 <= self.salary <= 20000:
            return 0.3 * (self.salary - 10000) + self.__progressive_tax(10000)
        elif 20001 <= self.salary <= 50000:
            return 0.4 * (self.salary - 20000) + self.__progressive_tax(20000)
        elif self.salary > 50_000:
            return 0.47 * (self.salary - 50000) + self.__progressive_tax(50000)
        return 0.0


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.workers = [
            (('Name', 1000), 0),
            (('Name', 2500), 150),
            (('Name', 6200), 752),
            (('Name', 15000), 3050),
            (('Name', 25000), 6550),
            (('Name', 100000), 40050)
        ]

    def test_progressive_tax(self):
        for worker, expected in self.workers:
            with self.subTest(query=worker):
                self.assertEqual(Worker(*worker).get_tax_value(), expected)

    @unittest.expectedFailure
    def test_neagitve_salary(self):
        Worker('Name', -1000)

    def tearDown(self) -> None:
        self.workers = []
