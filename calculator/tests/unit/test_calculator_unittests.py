import unittest

# from src.msd_module.string_manipulator import reverse_string
import calculator


class TestStringManipulator(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(calculator.hello(), "Hello world!")

    def test_addition(self):
        self.assertEqual(calculator.addition(1, 5), 6)
        self.assertEqual(calculator.addition(2, 4), 6)
        self.assertEqual(calculator.addition(3, 3), 6)
        self.assertEqual(calculator.addition(4, 2), 6)
        self.assertEqual(calculator.addition(5, 1), 6)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(5, 1), 4)
        self.assertEqual(calculator.subtraction(4, 2), 2)
        self.assertEqual(calculator.subtraction(3, 3), 0)
        self.assertEqual(calculator.subtraction(2, 4), -2)
        self.assertEqual(calculator.subtraction(1, 5), -4)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(1, 5), 5)
        self.assertEqual(calculator.multiplication(2, 4), 8)
        self.assertEqual(calculator.multiplication(3, 3), 9)
        self.assertEqual(calculator.multiplication(4, 2), 8)
        self.assertEqual(calculator.multiplication(5, 1), 5)

    def test_division(self):
        self.assertEqual(calculator.division(5, 1), 5)
        self.assertEqual(calculator.division(4, 1), 4)
        self.assertEqual(calculator.division(3, 1), 3)
        self.assertEqual(calculator.division(2, 1), 2)
        self.assertEqual(calculator.division(1, 1), 1)
