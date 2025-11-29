import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # -------- Addition Tests --------
    def test_addition(self):
        """Test addition with integers, negatives, zeros, and floats."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -3), -5)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(-2.5, 1.5), -1.0)

    # -------- Subtraction Tests --------
    def test_subtraction(self):
        """Test subtraction with integers, negatives, zeros, and floats."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-3, -2), -1)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        self.assertEqual(self.calc.subtract(-2.5, 1.5), -4.0)

    # -------- Multiplication Tests --------
    def test_multiplication(self):
        """Test multiplication with integers, negatives, zeros, and floats."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -4), 8)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(-1.5, 2), -3.0)

    # -------- Division Tests --------
    def test_division(self):
        """Test division with integers, negatives, zeros, floats, and division by zero."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(-7.5, 2.5), -3.0)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertIsNone(self.calc.divide(0, 0))  # 0/0 edge case

if __name__ == '__main__':
    unittest.main()
