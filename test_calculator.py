import unittest
from operations import add, sub, mul, div, power, squareroot, cube, mod
from parcer import analyse_input
from priority import between_parenthesis, power as op_power, square_root as op_square_root, mul_div, normal_cal
from calculation import calculate

class TestOperations(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(sub(5, 2), 3)
        self.assertEqual(mul(4, 3), 12)
        self.assertEqual(div(10, 2), 5.0)
        self.assertEqual(div(5, 0), "ERROR: Cannot divide by zero")
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(squareroot(9), 3.0)
        self.assertEqual(cube(3), 27)
        self.assertEqual(mod(5, 2), 1)

class TestParser(unittest.TestCase):
    def test_analyse_input(self):
        self.assertEqual(analyse_input("2 + 3"), [2.0, '+', 3.0])
        self.assertEqual(analyse_input("2 ** 3"), [2.0, '**', 3.0])
        self.assertEqual(analyse_input("9 //"), [9.0, '//'])
        self.assertEqual(analyse_input("(2 + 3) * 4"), ['(', 2.0, '+', 3.0, ')', '*', 4.0])
        self.assertEqual(analyse_input("invalid"), "ERROR: Invalid input")

class TestCalculationAndPriority(unittest.TestCase):
    def test_calculate_simple(self):
        self.assertEqual(calculate([2.0, '+', 3.0]), 5.0)
        self.assertEqual(calculate([2.0, '**', 3.0]), 8.0)
        self.assertEqual(calculate([9.0, '//']), 3.0)

    def test_precedence_no_parentheses(self):
        # 2 + 3 * 4 -> 14.0
        tokens = [2.0, '+', 3.0, '*', 4.0]
        tokens = op_power(tokens)
        tokens = op_square_root(tokens)
        tokens = mul_div(tokens)
        tokens = normal_cal(tokens)
        self.assertEqual(tokens, [14.0])

    def test_precedence_exponentiation(self):
        # 2 ** 3 * 2 -> 16.0
        tokens = [2.0, '**', 3.0, '*', 2.0]
        tokens = op_power(tokens)
        tokens = op_square_root(tokens)
        tokens = mul_div(tokens)
        tokens = normal_cal(tokens)
        self.assertEqual(tokens, [16.0])

    def test_square_root_precedence(self):
        # 9 // + 2 -> 5.0
        tokens = [9.0, '//', '+', 2.0]
        tokens = op_power(tokens)
        tokens = op_square_root(tokens)
        tokens = mul_div(tokens)
        tokens = normal_cal(tokens)
        self.assertEqual(tokens, [5.0])

    def test_parentheses(self):
        # (2 + 3) * 4 -> 20.0
        tokens = ['(', 2.0, '+', 3.0, ')', '*', 4.0]
        tokens = between_parenthesis(tokens)
        tokens = op_power(tokens)
        tokens = op_square_root(tokens)
        tokens = mul_div(tokens)
        tokens = normal_cal(tokens)
        self.assertEqual(tokens, [20.0])

if __name__ == '__main__':
    unittest.main()
