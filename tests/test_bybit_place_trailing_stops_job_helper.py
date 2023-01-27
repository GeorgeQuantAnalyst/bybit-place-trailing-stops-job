import unittest
import json
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from bybit_place_trailing_stops_job.bybit_place_trailing_stops_job_helper import BybitPlaceTrailingStopsJobHelper as Helper


class TestBybitPlaceTrailingStopsJobHelper(unittest.TestCase):

    POSITIONS_RAW_FILE_PATH = "tests/resources/positions_raw.json"
    POSITIONS_FILE_PATH = "tests/resources/positions.json"
    ACTIVE_POSITIONS_FILE_PATH = "tests/resources/active_positions.json"
    INSTRUMENTS_INFO_FILE_PATH = "tests/resources/instruments_info.json"

    def test_transform_positions(self):
        input = TestHelper.load_json(self.POSITIONS_RAW_FILE_PATH)
        expected_result = pd.DataFrame(TestHelper.load_json(self.POSITIONS_FILE_PATH))
        actual_result = Helper.transform_positions(input)

        assert_frame_equal(actual_result, expected_result)
    
    def test_parse_active_positions(self):
        input = {
            "positions" : pd.DataFrame(TestHelper.load_json(self.POSITIONS_FILE_PATH)),
            "instruments_info" : TestHelper.load_json(self.INSTRUMENTS_INFO_FILE_PATH)
        }

        expected_result = pd.DataFrame(TestHelper.load_json(self.ACTIVE_POSITIONS_FILE_PATH))
        actual_result = Helper.parse_active_positions(positions = input["positions"], instruments_info= input["instruments_info"])

        assert_frame_equal(actual_result.reset_index(drop=True), expected_result, check_index_type = False)

    def test_is_active_trailing_stop(self):
        self.assertTrue(Helper.is_active_trailing_stop(pd.Series({"symbol": "BTCUSDT", "trailing_stop": 567})))
        self.assertFalse(Helper.is_active_trailing_stop(pd.Series({"symbol": "BTCUSDT", "trailing_stop": 0})))

    def test_parse_price_scale(self):
        instruments_info = TestHelper.load_json(self.INSTRUMENTS_INFO_FILE_PATH)
        self.assertEqual(Helper.parse_price_scale(instruments_info=instruments_info, ticker="BTCUSDT"), 2)
        self.assertEqual(Helper.parse_price_scale(instruments_info=instruments_info, ticker="ETHUSDT"), 2)
        self.assertEqual(Helper.parse_price_scale(instruments_info=instruments_info, ticker="DOGEUSDT"), 5)
    

class TestHelper():

    def load_json(file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data


if __name__ == "__main__":
    unittest.main()