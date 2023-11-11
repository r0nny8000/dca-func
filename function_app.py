import datetime
import logging
import azure.functions as func
import dca_func.tools as tools


app = func.FunctionApp()

@app.function_name(name="dcahttp")
@app.route(route="dca", auth_level=func.AuthLevel.ANONYMOUS)
def hello_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("HTTP TRIGGER FUNCTION EXECUTED: %s", req.method)
    logging.info("TEST: " + tools.test())
    return func.HttpResponse("Hi")


@app.function_name(name="dcatimer")
@app.schedule(schedule="0 0 * * * *", arg_name="dcatimer", run_on_startup=False)
def dca_timer(dcatimer: func.TimerRequest) -> None:
    logging.info("TIMER FUNCTION EXECUTED: %s", datetime.datetime.utcnow())
    