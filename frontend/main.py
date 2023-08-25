import requests
from fastapi import FastAPI, Body
from utilities.logger import CustomLogging

# SAVE LOGS
logger = CustomLogging()
logger = logger.Create_Logger(file_name="main.log")

app = FastAPI()


def predict():
    """
    Function to make a prediction request to the front-end server.
    """
    url3 = "http://server.docker:8000/"
    logger.debug("Front-end prediction requested.")
    response = requests.request("GET", url3)
    response = response.text
    logger.debug("Front-end prediction obtained.")
    return response


def predict_rain_aus(input):
    """
    Function to make a prediction request to the prediction API.
    """
    url3 = "http://server.docker:8000/predict_rain"
    response = requests.post(url3, json=input)
    response = response.text
    return response


@app.get("/")
def read_root():
    """
    Endpoint for root route.
    """
    logger.info("Front-end is all ready to go!")
    return "Front-end is all ready to go!"


@app.post("/predict")
def predict(payload: dict = Body(...)):
    """
    Endpoint to make a prediction request using the prediction API.
    """
    logger.debug(f"Incoming input in the front end: {payload}")
    response = predict_rain_aus(payload)
    logger.debug(f"Prediction: {response}")
    return {"response": response}


@app.get("/healthcheck")
async def v1_healthcheck():
    """
    Endpoint for health check.
    """
    url3 = "http://server.docker:8000/"
    response = requests.request("GET", url3)
    response = response.text
    logger.info(f"Checking health: {response}")
    return response
