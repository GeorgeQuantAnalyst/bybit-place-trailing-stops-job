import logging
import logging.config

from bybit_place_trailing_stops_job.utils import load_config
from bybit_place_trailing_stops_job.constants import LOGGER_CONFIG_FILE_PATH, CONFIG_FILE_PATH, __logo__
from bybit_place_trailing_stops_job.bybit_place_trailing_stops_job import BybitPlaceTrailingStopsJob


if __name__ == "__main__":
    logging.config.fileConfig(
            fname=LOGGER_CONFIG_FILE_PATH, disable_existing_loggers=False)
    logging.info(__logo__)

    try:
        config = load_config(CONFIG_FILE_PATH)

        job = BybitPlaceTrailingStopsJob(config)
        job.run()
    except:
        logging.exception("Error in app: ")
