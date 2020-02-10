import os
import unittest
import saver as sv

class SaverIntegrationTest(unittest.TestCase):
    if not os.path.exists("test_data"):
        os.makedirs("test_data")

    def setUp(self):
        self.saver = sv.Saver('test_data/dataset.csv')

    def tearDown(self):
        self.saver.save()

    def test_add_records_to_file(self):
        records = [{"timestamp": 1581326626000, "value": 0.5}]

        self.saver.add(records)

if __name__ == '__main__':
    unittest.main()
