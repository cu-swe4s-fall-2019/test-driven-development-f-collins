import unittest
import math_lib as ml
import random
import statistics

class TestMathlib(unittest.TestCase):
    def test_list_mean_none(self):
        self.assertIsNone(ml.list_mean(None), None)

    def test_list_mean_empty_list(self):
        self.assertIsNone(ml.list_mean([]), None)

    def test_list_mean_one_list(self):
        self.assertEqual(ml.list_mean([1, 1, 1, 1, 1]), 1)

    def test_list_mean_random_int_list(self):
        for i in range(100):
            L = []
            for j in range(10):
                L.append(random.randint(0,100))
            self.assertEqual(ml.list_mean(L), statistics.mean(L))

    def test_list_mean_random_float_list(self):
        for i in range(100):
            L = []
            for j in range(10):
                L.append(random.uniform(0,100))
            self.assertAlmostEqual(ml.list_mean(L), statistics.mean(L))

    def test_list_mean_non_number_in_list(self):
        L = []
        for j in range(10):
            L.append(random.uniform(0,100))
        mean = statistics.mean(L)
        L.append('x')
        random.shuffle(L)
        self.assertAlmostEqual(ml.list_mean(L), mean)



if __name__ == "__main__":
    unittest.main()

