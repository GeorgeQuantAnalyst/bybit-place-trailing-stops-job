import pandas as pd
import logging


class BybitPlaceTrailingStopsJobHelper():

    DEFAULT_PRICE_SCALE = 2

    @staticmethod
    def transform_positions(positions_raw: dict) -> pd.DataFrame:
        result = []

        for position in positions_raw["result"]:
            result.append(position["data"])

        return pd.DataFrame(result)

    @staticmethod
    def parse_active_positions(positions: pd.DataFrame, instruments_info: dict) -> pd.DataFrame:
        active_positions = positions[positions["position_value"] > 0]
        active_positions["price_scale"] = active_positions.apply(
            lambda row: BybitPlaceTrailingStopsJobHelper.parse_price_scale(instruments_info, row["symbol"]), axis=1)

        if not active_positions.empty:
            active_positions["is_set_stop_loss"] = active_positions["stop_loss"] > 0
            active_positions["compute_trailing_stop"] = abs(
                active_positions["entry_price"] - active_positions["stop_loss"])
            active_positions["compute_trailing_stop"] = active_positions.apply(
                lambda x: round(x["compute_trailing_stop"], x["price_scale"]), axis=1)

        return active_positions

    @staticmethod
    def place_trailing_stops(active_positions: pd.DataFrame, exchange) -> None:

        for index, active_position in active_positions.iterrows():
            if BybitPlaceTrailingStopsJobHelper.is_active_trailing_stop(active_position):
                logging.info("The Position {}-{} position already has a trailing stop.".format(
                    active_position["symbol"], active_position["side"]))
                continue

            if active_position["is_set_stop_loss"] == False:
                logging.error("The Position {}-{} does not have a hard stop loss set. Job cannot set traling stop loss.".format(
                    active_position["symbol"], active_position["side"]))
                continue

            try:
                exchange.set_trading_stop(
                    symbol=active_position["symbol"],
                    side=active_position["side"],
                    trailing_stop=active_position["compute_trailing_stop"],
                    position_idx=0
                )
                logging.info("Successfull place trailing stop for position {}-{}".format(
                    active_position["symbol"], active_position["side"]))
            except Exception as e:
                logging.exception("Problem with place trailing stop for {}-{} on exchange Bybit".format(
                    active_position["symbol"], active_position["side"]))

    @staticmethod
    def is_active_trailing_stop(position) -> bool:
        return position["trailing_stop"] > 0

    @staticmethod
    def parse_price_scale(instruments_info: dict, ticker: str) -> float:
        instruments_info_list = instruments_info["result"]["list"]
        price_scale = [x["priceScale"]
                       for x in instruments_info_list if x["symbol"] == ticker]
        return int(price_scale[0]) if any(price_scale) else BybitPlaceTrailingStopsJobHelper.DEFAULT_PRICE_SCALE
