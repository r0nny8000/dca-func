import pytest
import dca_func.market_data as market_data
import logging

def test_get_coin_information():
    logging.info("start test logging")
    logging.info(market_data.get_coin_information("BTCUSDT"))
    logging.info(market_data.get_coin_information("BTCEUR"))
