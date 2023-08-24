# Rain in Australia
In this project for MLOps we're working with this dataset for apply the acquire in class knowlegge.

### About Dataset
This dataset contains about 10 years of daily weather observations from many locations across Australia. Predict next-day rain by training classification models on the target variable RainTomorrow.

RainTomorrow is the target variable to predict. It means -- did it rain the next day, Yes or No? This column is Yes if the rain for that day was 1mm or more.

### Dataset Information
- Number of Instances: 145,460
- Number of Features: 23
- Target Variable: RainTomorrow

### Solution
In this project we will show we will work with a notebook downloaded from the Kaggle platform, in this solution they propose to use an artificial neural network. The process includes loading data, visualizing the data, cleaning the data, preprocessing the data and building the model.

In addition to the above, we will work with the code to apply refactorization, docstrings, annotation and some other best practices in a correct management of a MLOps project. The project going to up to github platform for colaborate with others parthers if that is necesary.


## Setup
### Activate virtual environment
1. Create a virtual environment with `Python 3.10+`
    * Create venv
        ```bash
        python3.10 -m venv venv_project
        ```

    * Activate the virtual environment
        ```
        venv_project\Scripts\activate
        ```
    * Install the packages
        ```bash
        pip install -r requirements.txt
        ```

## Execution of unit tests (Pytest)

### Test location

You can find the test location in the [test](test) folder, and the following tests:

* Test `test_csv_file_existence`:  
Test case to check if the CSV file exists.

* Test `test_model_existence`:  
Test to validate the existence of a `.h5` model file.

### Execution instructions

#### Test CSV file existence

The following test validates the CSV file existence before the training.

Follow the next steps to run the test.
* Run in the terminal:

    ```bash
    pytest ./test/test_data.py::test_csv_file_existence -v -s
    ```
* You should see the following data output:
    ```pytest
    ================================================================================================ test session starts =================================================================================================
    platform win32 -- Python 3.10.11, pytest-7.4.0, pluggy-1.2.0 -- C:\Users\fzavala\Documents\GitHub\Final-project\venv_project\Scripts\python.exe
    cachedir: .pytest_cache
    rootdir: C:\Users\fzavala\Documents\GitHub\Final-project
    plugins: anyio-3.7.1
    collected 1 item

    test/test_data.py::test_csv_file_existence PASSED

    ================================================================================================= 1 passed in 1.00s ==================================================================================================
    ```

#### Test model existence

The following test validates the model's existence after the training.

Follow the next steps to run the test.
* Run in the terminal:

    ```bash
    pytest ./test/test_data.py::test_model_existence -v -s
    ```

* You should see the following data output:
    ```pytest
    ================================================================================================ test session starts =================================================================================================
    platform win32 -- Python 3.10.11, pytest-7.4.0, pluggy-1.2.0 -- C:\Users\fzavala\Documents\GitHub\Final-project\venv_project\Scripts\python.exe
    cachedir: .pytest_cache
    rootdir: C:\Users\fzavala\Documents\GitHub\Final-project
    plugins: anyio-3.7.1
    collected 1 item

    test/test_data.py::test_model_existence ./models\model.h5
    PASSED

    ================================================================================================= 1 passed in 0.76s ==================================================================================================
    ```

## Usage

### Individual Fastapi and Use Deployment

* Run the next command to start the RainAUS API locally

    ```bash
    uvicorn API.main:app --reload
    ```


