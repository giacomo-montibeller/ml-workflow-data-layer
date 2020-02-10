import unittest
import datetime as dt
import app

class AppTest(unittest.TestCase):
    def test_configs_extraction(self):
        configs = app.get_configs_from("test_config.json")

        self.assertEqual(configs["category"], "category")
        self.assertEqual(configs["data_type"], "data type")
        self.assertEqual(configs["time_from"], "2020-01-01")
        self.assertEqual(configs["time_to"], "2020-01-05")
        self.assertEqual(configs["time_frame_size"], 1)

    def test_time_framer(self):
        time_from = dt.datetime(2020, 1, 1)
        time_to = dt.datetime(2020, 1, 31)
        time_frame_size = 2

        time_frames = app.time_frames_from(time_from, time_to, time_frame_size)

        self.assertEqual(16, len(time_frames))

    def test_date_from_string(self):
        date_as_string = "2020-02-01"

        parsed_date = app.date_from(date_as_string)

        self.assertEqual(2020, parsed_date.year)
        self.assertEqual(2, parsed_date.month)
        self.assertEqual(1, parsed_date.day)

if __name__ == '__main__':
    unittest.main()
