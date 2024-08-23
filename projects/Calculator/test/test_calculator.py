# test/test_calculator.py
import unittest
# Adjust the import path based on your project structure
from ..projects.calculator1 import is_valid
 
 

class TestIsValid(unittest.TestCase):

    def test_valid_input(self):
        self.assertTrue(is_valid("1+2+"))
        self.assertTrue(is_valid("4*(2/2)^3"))
        self.assertTrue(is_valid("1 + 2"))
        self.assertTrue(is_valid("10%2"))
        self.assertTrue(is_valid("(1+2)*(3-4)"))

    def test_invalid_input(self):
        self.assertFalse(is_valid("1+2+a"))
        self.assertFalse(is_valid("4*(2/2)^3&"))
        self.assertFalse(is_valid("1 + 2!"))
        self.assertFalse(is_valid("a10%2"))
        self.assertFalse(is_valid("(1+2)*(3-4]"))

if __name__ == '__main__':
    unittest.main()
