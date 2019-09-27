import unittest
import math_lib as ml

class TestMathlib(unittest.TestCase):
    def test_list_mean_none(self):
        self.assertIsNone(ml.list_mean(None), None)

if __name__ == "__main__":
    unittest.main()

