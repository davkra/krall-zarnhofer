import unittest
import calculator


class TestStringManipulator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.calculate(1, 5, "add"), 6)
        self.assertEqual(calculator.calculate(2, 4, "add"), 6)
        self.assertEqual(calculator.calculate(3, 3, "add"), 6)
        self.assertEqual(calculator.calculate(4, 2, "add"), 6)
        self.assertEqual(calculator.calculate(5, 1, "add"), 6)

    def test_subtraction(self):
        self.assertEqual(calculator.calculate(5, 1, "subtract"), 4)
        self.assertEqual(calculator.calculate(4, 2, "subtract"), 2)
        self.assertEqual(calculator.calculate(3, 3, "subtract"), 0)
        self.assertEqual(calculator.calculate(2, 4, "subtract"), -2)
        self.assertEqual(calculator.calculate(1, 5, "subtract"), -4)
