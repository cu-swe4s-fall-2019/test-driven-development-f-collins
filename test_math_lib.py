import unittest
import math_lib as ml

class TestMathlib(unittest.TestCase):
    def test_list_mean_none(self):
        self.assertIsNone(ml.list_mean(None), None)

    def test_list_mean_empty_list(self):
        self.assertIsNone(ml.list_mean([]), None)

    def test_list_mean_one_list(self):
        self.assertEqual(ml.list_mean([1, 1, 1, 1, 1]), 1)

if __name__ == "__main__":
    unittest.main()

