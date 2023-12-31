import argparse
from keras.models import load_model
from utilities.logger import CustomLogging

#SAVE LOGS
logger = CustomLogging()
logger = logger.Create_Logger(file_name="predictor/predict.log")

class ModelPredictor:
    """
    A class to load a trained machine learning model and make predictions on new data.

    Parameters:
        model_path (str): Path to the trained model file (load_model format).

    Methods:
        predict(new_data):
            Makes predictions on the provided new_data using the loaded model.

    Usage:
        $ python model.py models/model.h5 path_to_new_data
    """

    def __init__(self, model_path):
        """
        Initializes the ModelPredictor instance.

        Parameters:
            model_path (str): Path to the trained model file (load_model format).
        """
        self.model = load_model(model_path)

    def predict(self, new_data):
        """
        Makes predictions on the provided new_data using the loaded model.

        Parameters:
            new_data: The data on which to make predictions.

        Returns:
            Predicted outputs from the model.
        """
        return self.model.predict(new_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Model Predictor')
    parser.add_argument('model_path', type=str, help='Path to the trained model file')
    parser.add_argument('new_data', type=str, help='Path to the file containing new data for prediction')
    args = parser.parse_args()

    predictor = ModelPredictor(args.model_path)

    new_data = args.new_data

    predictions = predictor.predict(new_data)
    logger.info("prediction was genrated successfully.")
    print(predictions)