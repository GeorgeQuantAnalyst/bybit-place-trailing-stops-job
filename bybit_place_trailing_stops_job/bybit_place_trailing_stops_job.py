import logging.config
import logging
from pybit import usdt_perpetual
import requests
import pandas as pd
from bybit_place_trailing_stops_job.bybit_place_trailing_stops_job_helper import BybitPlaceTrailingStopsJobHelper as Helper

class BybitPlaceTrailingStopsJob:

    DEFAULT_PRICE_SCALE = 2

    def __init__(self, config: dict) -> None:
        self.config = config
        self.exchange = usdt_perpetual.HTTP(
            endpoint=config["exchangeApi"]["endpoint"],
            api_key=config["exchangeApi"]["apiKey"],
            api_secret=config["exchangeApi"]["secretKey"]
        )

    def run(self) -> None:
        logging.info("Start job")

        logging.info("Loading data")
        positions_raw = self.exchange.my_position()
        logging.debug("Positions_raw: {}".format(positions_raw))

        instruments_info = requests.get(
            self.config["exchangeApi"]["instrumentInfoEndpoint"]).json()
        logging.debug("Instruments_info: {}".format(instruments_info))

        logging.info("Transform position")
        positions = Helper.transform_positions(positions_raw)
        logging.info("Total positions: {}".format(positions.shape[0]))
        logging.debug("Positions: {}".format(positions.to_json()))

        logging.info("Parse active position")
        active_positions = Helper.parse_active_positions(
            positions, instruments_info)
        logging.info("Count active positions: {}".format(
            active_positions.shape[0]))
        logging.debug("Active positions: {}".format(
            active_positions.to_json()))

        if not active_positions.empty:
            logging.info("Place trailing stops")
            Helper.place_trailing_stops(active_positions, self.exchange)

        logging.info("Finished job")