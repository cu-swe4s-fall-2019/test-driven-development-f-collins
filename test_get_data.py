import unittest
import get_data as gt

class TestGetData(unittest.TestCase):
    def test_read_stdin_col_none(self):
        self.assertIsNone(gt.read_stdin_col(None), None)

if __name__ == "__main__":
    unittest.main()
