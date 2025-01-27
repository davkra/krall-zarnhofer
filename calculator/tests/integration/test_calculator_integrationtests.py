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

    def test_multiplication(self):
        self.assertEqual(calculator.calculate(1, 5, "multiply"), 5)
        self.assertEqual(calculator.calculate(2, 4, "multiply"), 8)
        self.assertEqual(calculator.calculate(3, 3, "multiply"), 9)
        self.assertEqual(calculator.calculate(4, 2, "multiply"), 8)
        self.assertEqual(calculator.calculate(5, 1, "multiply"), 5)

    def test_division(self):
        self.assertEqual(calculator.calculate(5, 1, "divide"), 5)
        self.assertEqual(calculator.calculate(4, 1, "divide"), 4)
        self.assertEqual(calculator.calculate(3, 1, "divide"), 3)
        self.assertEqual(calculator.calculate(2, 1, "divide"), 2)
        self.assertEqual(calculator.calculate(1, 1, "divide"), 1)
