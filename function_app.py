import datetime
import logging
import azure.functions as func
import dca_func.tools as tools
import bitget.v2.spot.market_api as market_api


app = func.FunctionApp()

@app.function_name(name="dcahttp")
@app.route(route="dca", auth_level=func.AuthLevel.ANONYMOUS)
def hello_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("HTTP TRIGGER FUNCTION EXECUTED: %s", req.method)
    logging.info("TEST: " + tools.test())
    return func.HttpResponse("Hi. This is a test :" + tools.test())

@app.function_ame(name="dcabitgetcoins")
@app.route(route="coins", auth_level=func.AuthLevel.ANONYMOUS)
def coins_function(req: func.HttpRequest) -> func.HttpResponse:
    apiKey = "apiKey"
    secretKey = "secretKey"
    passphrase = "passphrase"

    market = market_api.MarketApi(apiKey, secretKey, passphrase)

    try:

        params = {}
        params["coin"] = "BTC"

        response = market.coins(params)
        return func.HttpResponse(response)

    except BitgetAPIException as e:
        return func.HttpResponse("Error: " + e.message)

    return func.HttpResponse("The end.")
    

@app.function_name(name="dcatimer")
@app.schedule(schedule="0 0 * * * *", arg_name="dcatimer", run_on_startup=False)
def dca_timer(dcatimer: func.TimerRequest) -> None:
    logging.info("TIMER FUNCTION EXECUTED: %s", datetime.datetime.utcnow())
    