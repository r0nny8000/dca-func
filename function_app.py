import datetime
import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="dcatimer")
@app.schedule(schedule="00:00:16", arg_name="dcatimer", run_on_startup=False)
def dca_timer(timer: func.TimerRequest) -> None:
    logging.info("FUNCTION EXECUTED: %s", datetime.datetime.utcnow())
    