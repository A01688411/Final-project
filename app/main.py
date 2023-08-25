import os
import sys
from fastapi import FastAPI
from starlette.responses import JSONResponse
from predictor.predict import ModelPredictor
from models.models import RainAUS
from utilities.logger import CustomLogging

# SAVE LOGS
logger = CustomLogging()
logger = logger.Create_Logger(file_name="main.log")

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

app = FastAPI()

@app.get('/', status_code=200)
async def healthcheck():
    """
    Endpoint for health check.
    """
    logger.info("Rain predictor is all ready to go!")
    return 'Rain predictor is all ready to go!'

@app.post('/predict_rain')
def predictor(rain_aus_features: RainAUS) -> JSONResponse:
    """
    Endpoint to make predictions for rain based on provided weather features.
    """
    predictor = ModelPredictor("ml_models/model.h5")
    X = [rain_aus_features.Cloud3pm,
         rain_aus_features.Cloud9am,
         rain_aus_features.Evaporation,
         rain_aus_features.Humidity3pm,
         rain_aus_features.Humidity9am,
         rain_aus_features.Location,
         rain_aus_features.MaxTemp,
         rain_aus_features.MinTemp,
         rain_aus_features.Pressure3pm,
         rain_aus_features.Pressure9am,
         rain_aus_features.Rainfall,
         rain_aus_features.Sunshine,
         rain_aus_features.Temp3pm,
         rain_aus_features.Temp9am,
         rain_aus_features.WindGustSpeed,
         rain_aus_features.WindSpeed3pm,
         rain_aus_features.WindSpeed9am,
         rain_aus_features.day_cos,
         rain_aus_features.day_sin,
         rain_aus_features.month_cos,
         rain_aus_features.month_sin,
         rain_aus_features.year]
    #print([X])
    prediction = predictor.predict([X])
    logger.debug("The prediction was created.")
    return JSONResponse(f"Resultado predicción")


