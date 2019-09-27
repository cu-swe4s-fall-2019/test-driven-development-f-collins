import unittest
import data_viz as dv

class TestDataViz(unittest.TestCase):
    def test_boxplot_file_name_none(self):
        self.assertIsNone(dv.boxplot(None, None), None)
        
    def test_histogram_file_name_none(self):
        self.assertIsNone(dv.histogram(None, None), None)

    def test_combo_file_name_none(self):
        self.assertIsNone(dv.combo(None, None), None)

if __name__ == "__main__":
    unittest.main()
