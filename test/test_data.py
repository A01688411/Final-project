import os
import pytest
import pandas as pd

def does_csv_file_exist(file_path):
    """
    Check if a CSV file exists at the specified path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def test_csv_file_existence():
    """
    Test case to check if the CSV file exists.
    """
    # Provide the path to the CSV file that needs to be tested
    csv_file_path = "Final-project/data/weatherAUS.csv"
    
    DATASETS_DIR = './data/'
    
    #URL = 'https://github.com/A01688411/project-MLOPS/blob/11c06cd85433342f397f13e6fd3192964ae85402/data/weatherAUS.csv'
    #data_retriever = DataRetriever(URL, DATASETS_DIR)
    #data_retriever.retrieve_data()

    # Call the function to check if the CSV file exists
    file_exists = does_csv_file_exist(csv_file_path)

    # Use Pytest's assert statement to check if the file exists
    assert file_exists == False, f"The CSV file at '{csv_file_path}' does not exist."

def test_model_existence():
    """
    Test to validate the existence of a .h5 model file.

    This test function checks whether the specified .h5 model file exists
    in the specified directory.

    Raises:
        AssertionError: If the model file doesn't exist.

    Usage:
        Run this test using the pytest command:
        pytest test_data.py
    """
    model_filename = "model.h5"
    MODEL_DIRECTORY = "./models"
    model_path = os.path.join(MODEL_DIRECTORY, model_filename)
    print(model_path)
    assert os.path.exists(model_path), f"Model file '{model_filename}' does not exist."

if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])



