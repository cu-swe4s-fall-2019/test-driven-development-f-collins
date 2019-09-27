import unittest
import math_lib as ml

class TestMathlib(unittest.TestCase):
    def test_list_mean_none(self):
        self.assertIsNone(ml.list_mean(None), None)

    def test_list_mean_empty_list(self):
        self.assertIsNone(ml.list_mean([]), None)

if __name__ == "__main__":
    unittest.main()

