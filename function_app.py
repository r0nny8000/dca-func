import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("test function hello executed")
    return func.HttpResponse("HttpTrigger1 function processed a request!")
    