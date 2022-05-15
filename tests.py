import unittest

from factorial_recursion import compute_factorial


class FactorialTest(unittest.TestCase):

    def test_simple_number(self):
        expected_result = 5040
        result = compute_factorial(7)

        self.assertEqual(expected_result, result)

    def test_stack_overflow(self):
        self.assertRaises(RecursionError, compute_factorial, 1000)

    def test_negative_number(self):
        self.assertRaises(BaseException, compute_factorial, -1)
