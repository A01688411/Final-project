from pydantic import BaseModel


class rainAUS(BaseModel):
    """
    Represents a passenger on the Titanic with various attributes.
    
    Attributes:
        pclass_nan (float): Placeholder for missing values in 'pclass' attribute.
        age_nan (float): Placeholder for missing values in 'age' attribute.
        sibsp_nan (float): Placeholder for missing values in 'sibsp' attribute.
        parch_nan (float): Placeholder for missing values in 'parch' attribute.
        fare_nan (float): Placeholder for missing values in 'fare' attribute.
        sex_male (float): Placeholder for 'sex' attribute being male.
        cabin_Missing (float): Placeholder for 'cabin' attribute being missing.
        cabin_rare (float): Placeholder for 'cabin' attribute being rare.
        embarked_Q (float): Placeholder for 'embarked' attribute being Queenstown.
        embarked_S (float): Placeholder for 'embarked' attribute being Southampton.
        title_Mr (float): Placeholder for 'title' attribute being Mr.
        title_Mrs (float): Placeholder for 'title' attribute being Mrs.
        title_rar (float): Placeholder for 'title' attribute being rare.
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
    #RainTomorrow: float
    
    #MinTemp: float
    #MaxTemp: float
    #Rainfall: float
    #Evaporation: float
    #Sunshine: float
    #WindGustSpeed: float
    #WindSpeed9am: float
    #WindSpeed3pm: float
    #Humidity9am: float
    #Humidity3pm: float
    #Pressure9am: float
    #Pressure3pm: float
    #Cloud9am: float
    #Cloud3pm: float
    #Temp9am: float
    #Temp3pm: float