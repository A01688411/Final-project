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

#### Checking endpoints

1. Access `http://127.0.0.1:8000/`, you will see a message like this `"Rain predictor is all ready to go!"`
2. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:
![FastAPI Docs](docs\img\FastAPI.PNG)
3. Try running the following predictions with the endpoint by writing the following values:
    * **Prediction 1**  
        Request body

        ```bash
        {
        "Cloud3pm": 0.1,
        "Cloud9am": 1.4,
        "Evaporation": 0.1,
        "Humidity3pm": -0.1,
        "Humidity9am": -1.4,
        "Location": 0.1,
        "MaxTemp": -1.5,
        "MinTemp": -0.0,
        "Pressure3pm": 0.1,
        "Pressure9am": -1.2,
        "Rainfall": -1.4,
        "Sunshine": -0.2,
        "Temp3pm": 0.1,
        "Temp9am": 0.0,
        "WindGustSpeed": -0.0,
        "WindSpeed3pm": 0.3,
        "WindSpeed9am": 0.6,
        "day_cos": 0.6,
        "day_sin": 1.4,
        "month_cos": 0.2,
        "month_sin": 1.4,
        "year": -0.0
        }
        ```

        Response body         
        The output will be:
        ```bash
        "Resultado predicción: [[0.00278837]]"
        ```


    * **Prediction 2**  
        Request body

        ```bash
        {
        "Cloud3pm": 0.1,
        "Cloud9am": 1.4,
        "Evaporation": 0.1,
        "Humidity3pm": -0.1,
        "Humidity9am": -1.4,
        "Location": 0.1,
        "MaxTemp": -1.5,
        "MinTemp": -0.0,
        "Pressure3pm": 0.1,
        "Pressure9am": -1.2,
        "Rainfall": -1.4,
        "Sunshine": -0.2,
        "Temp3pm": 0.1,
        "Temp9am": 0.0,
        "WindGustSpeed": -0.0,
        "WindSpeed3pm": 0.3,
        "WindSpeed9am": 0.6,
        "day_cos": 0.6,
        "day_sin": 1.4,
        "month_cos": 0.2,
        "month_sin": 1.4,
        "year": -0.0
        }
        ```

        Response body         
        The output will be:
        ```bash
        "Resultado predicción: [[0.73788786]]"
        ```
### Individual deployment of the API with Docker and usage

#### Build the image

* Ensure you are in the `Final-project/` directory (root folder).
* Run the following code to build the image:
    ```bash
    docker build -t rainaus-image ./app/
    ```

* Inspect the image created by running this command:

    ```bash
    docker images
    ```
    Output:
    ```bash
    REPOSITORY      TAG       IMAGE ID       CREATED         SIZE
    rainaus-image   latest    a738560a549e   2 minutes ago   495MB
    ```

#### Run Titanic REST API

1. Run the next command to start the `rainaus-image` image in a container.
    ```bash
    docker run -d --name rainaus-c -p 8000:8000 rainaus-image
    ```
2. Check the container running.

    ```bash
    docker ps -a
    ```
    Output:

    ```bash
    CONTAINER ID   IMAGE           COMMAND                  CREATED              STATUS                          PORTS                    NAMES
    b9e5b770938b   rainaus-image   "uvicorn main:app --…"   About a minute ago   Exited (1) About a minute ago                            rainaus-c
    ```
#### Checking endpoints for app

1. Access `http://127.0.0.1:8000/`, and you will see a message like this `"Titanic classifier is all ready to go!"`
2. A file called `main_api.log` will be created automatically inside the container. We will inspect it below.
3. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:
    ![FastAPI Docs](docs/imgs/fast-api-docs.png)

4. Try running the following predictions with the endpoint by writing the following values:


