import datetime
import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="dcatimer")
@app.schedule(schedule="0 0 * * * *", arg_name="dcatimer", run_on_startup=False)
def dca_timer(dcatimer: func.TimerRequest) -> None:
    logging.info("FUNCTION EXECUTED: %s", datetime.datetime.utcnow())
    