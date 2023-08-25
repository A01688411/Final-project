from pydantic import BaseModel


class RainAUS(BaseModel):
    """
    Represents weather data in Australia with various attributes.
    """

    Cloud3pm: float  # Cloud coverage at 3 PM
    Cloud9am: float  # Cloud coverage at 9 AM
    Evaporation: float  # Evaporation rate
    Humidity3pm: float  # Humidity at 3 PM
    Humidity9am: float  # Humidity at 9 AM
    Location: float  # Location identifier
    MaxTemp: float  # Maximum temperature
    MinTemp: float  # Minimum temperature
    Pressure3pm: float  # Atmospheric pressure at 3 PM
    Pressure9am: float  # Atmospheric pressure at 9 AM
    Rainfall: float  # Rainfall amount
    Sunshine: float  # Sunshine duration
    Temp3pm: float  # Temperature at 3 PM
    Temp9am: float  # Temperature at 9 AM
    WindGustSpeed: float  # Maximum wind gust speed
    WindSpeed3pm: float  # Wind speed at 3 PM
    WindSpeed9am: float  # Wind speed at 9 AM
    day_cos: float  # Cosine of the day of the year
    day_sin: float  # Sine of the day of the year
    month_cos: float  # Cosine of the month of the year
    month_sin: float  # Sine of the month of the year
    year: float  # Year
