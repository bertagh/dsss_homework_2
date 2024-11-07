import unittest
from math_quiz import random_number, random_operator, operation


class TestMathGame(unittest.TestCase):

    def test_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # Test if random_operator generates one of the allowed operators
        operators = ['+', '-', '*']
        for _ in range(100):  # Test multiple times to cover randomness
            operator = random_operator()
            self.assertIn(operator, operators, f"Generated operator {operator} is not valid")

    def test_operation(self):
        '''Tests the 'operation' function to ensure it returns the correct operation string 
        and computes the correct result for different operators (+, -, *)'''
        test_cases = [
            (3, 2, '+', '3 + 2', 5),
            (6, 3, '-', '6 - 3', 3),
            (4, 5, '*', '4 * 5', 20)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            operation_text, answer = operation(num1, num2, operator)
            self.assertEqual(operation_text, expected_problem, f"Expected problem {expected_problem} but got {operation_text}")
            self.assertEqual(answer, expected_answer, f"Expected answer {expected_answer} but got {answer}")

if __name__ == "__main__":
    unittest.main()
