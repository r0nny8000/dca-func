import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpTrigger1")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("TEST FUNCTION EXECUTED AFTER: %s", req.method)
    return func.HttpResponse("HttpTrigger1 function processed a request after deploying via Github Action!")
    