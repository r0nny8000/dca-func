import logging

from bitget.v2.spot.market_api import MarketApi 
from bitget.exceptions import BitgetAPIExceptionln 


def get_coin_information(symbol: str): 

    logging.debug("get coin informations")

    apiKey = "apiKey"
    secretKey = "secretKey"
    passphrase = "passphrase"

    market = MarketApi(apiKey, secretKey, passphrase)

    try:

        params = {}
        params["symbol"] = symbol

        return market.tickers(params)
        

    except BitgetAPIException as e:
        return e.message

    return "nothing happed"
