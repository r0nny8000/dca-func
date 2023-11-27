import function_app
import azure.functions as func

def test_hello_function():
    req = func.HttpRequest("GET", "https://www.bea2b.de", bytes())
    assert hello_function(req) != None