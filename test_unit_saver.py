import unittest
import saver as sv

class SaverTest(unittest.TestCase):
    def test_get_hours_from_timestamp(self):
        timestamp = 1577872800000

        hours = sv.hour_from_timestamp(timestamp)

        self.assertEqual(hours, 11)

if __name__ == '__main__':
    unittest.main()
