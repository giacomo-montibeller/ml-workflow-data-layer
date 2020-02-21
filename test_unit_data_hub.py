import unittest
import data_hub

class DataHubTest(unittest.TestCase):
    def test_assert_true_if_valid_location(self):
        latitude = 46.48
        longitude = 11.30
        station = {"latitude": latitude, "longitude": longitude}

        is_valid_location = data_hub.valid_location(station)

        self.assertEqual(True, is_valid_location)

    def test_assert_false_if_invalid_location(self):
        latitude = 40
        longitude = 20
        station = {"latitude": latitude, "longitude": longitude}

        is_valid_location = data_hub.valid_location(station)

        self.assertEqual(False, is_valid_location)

    def test_build_url(self):
        category = "any_category"
        operation = "any_operation"
        query_string = "any_query_string"

        url = data_hub.url_for(category, operation, query_string)

        self.assertEqual("http://ipchannels.integreen-life.bz.it/any_category/rest/any_operation?any_query_string", url)

if __name__ == '__main__':
    unittest.main()
