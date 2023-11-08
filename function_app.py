import logging
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="Hello")
@app.route(route="hello", auth_level=func.AuthLevel.ANONYMOUS)
def hello_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("TEST FUNCTION EXECUTED AFTER: %s", req.method)
    return func.HttpResponse("Hello function processed a request after deploying via Github Action!")
    

@app.function_name(name="World")
@app.route(route="world", auth_level=func.AuthLevel.ANONYMOUS)
def hello_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("TEST FUNCTION EXECUTED AFTER: %s", req.method)
    return func.HttpResponse("World function processed a request after deploying via Github Action!")
