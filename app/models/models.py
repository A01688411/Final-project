from pydantic import BaseModel


class rainAUS(BaseModel):
    """
    Represents a weather in AUS with various attributes.
    """

    Cloud3pm: float
    Cloud9am: float
    Evaporation: float
    Humidity3pm: float
    Humidity9am: float
    Location: float
    MaxTemp: float
    MinTemp: float
    Pressure3pm: float
    Pressure9am: float
    Rainfall: float
    Sunshine: float
    Temp3pm: float
    Temp9am: float
    WindGustSpeed: float
    WindSpeed3pm: float
    WindSpeed9am: float
    day_cos: float
    day_sin: float
    month_cos: float
    month_sin: float
    year: float