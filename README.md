# Turnover API

# Welcome to turnover API!

This API enables real-time generation of accumulated turnover for a
given username. From its registration date, the model predicts the
accumulated turnover over 30, 45, 60 and 90 days ahead using a machine
learning model.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Endpoints](#endpoints)
  - [Endpoint 1](#endpoint-1)
- [Authors](#authors)

## Getting Started <a name="getting-started"></a>

### Prerequisites <a name="prerequisites"></a>

This API is written in Python. In order to set up all dependencies, it
is essential you to use the Python virtualenv management tool
[`pipenv`](https://pipenv.pypa.io/en/latest/).

### Installation <a name="installation"></a>

Once you clone this repository, go the API directory. There will be a
file called `Pipfile.lock` specifying all the dependencies used. Open a
terminal and run the following command:

    pipenv sync

This command will install all the packages and their respective versions
necessary to run the API.

### Usage <a name="usage"></a>

Once the environment is set up, we can run the API as follows:

    pipenv run python api.py

## Endpoints <a name="endpoints"></a>

### Endpoint 1 <a name="endpoint-1"></a>

- **URL**: `/predict_turnover`

- **Method**: POST

- **Description**: This endpoint will calculate the prediction for the
  accumulated turnover for each user for the next 30, 45, 60 and 90
  days.

- **Input**: `JSON` file containing the following information for each
  user:

  - `Username`: the username;
  - `age`: age at the time of registration;
  - `turnover_accum_lag_1`: accumulated turnover on the first day after
    registration;
  - `turnover_accum_lag_2`: accumulated turnover on the second day after
    registration;
  - `turnover_accum_lag_3`: accumulated turnover on the third day after
    registration;
  - `turnover_accum_lag_4`: accumulated turnover on the fourth day after
    registration;
  - `turnover_accum_lag_5`: accumulated turnover on the fifth day after
    registration;

  For example:  
  `[{"Username":"ande2903","Amount":100.0,"age":37.0,"turnover_accum_lag_1":8.0,"turnover_accum_lag_2":8.0,"turnover_accum_lag_3":8.0,"turnover_accum_lag_4":48.0,"turnover_accum_lag_5":79.0},{"Username":"fernanda261067","Amount":5.0,"age":35.0,"turnover_accum_lag_1":23.1,"turnover_accum_lag_2":23.1,"turnover_accum_lag_3":23.1,"turnover_accum_lag_4":23.1,"turnover_accum_lag_5":23.1}]`

- **Response**:

  - JSON with the accumulated turnover over the next 30, 45, 60 and 90
    days for each user.

  For example:
  `[{"Username":"erika12144","turnover_accum_30_pred":17.4625242857,"turnover_accum_45_pred":31.7690522222,"turnover_accum_60_pred":31.7690522222,"turnover_accum_90_pred":31.7690522222},{"Username":"euphobravo","turnover_accum_30_pred":30.3746,"turnover_accum_45_pred":39.5762666667,"turnover_accum_60_pred":39.5762666667,"turnover_accum_90_pred":43.75004},{"Username":"ande2903","turnover_accum_30_pred":653.76418,"turnover_accum_45_pred":1134.79246,"turnover_accum_60_pred":1366.29176,"turnover_accum_90_pred":1366.29176},{"Username":"fernanda261067","turnover_accum_30_pred":23.20394,"turnover_accum_45_pred":23.20394,"turnover_accum_60_pred":23.20394,"turnover_accum_90_pred":23.20394}]`

## Examples <a name="examples"></a>

There is a file called `test.json` in this repository that contains an
example of the input format this API accept.

Suppose you are running the API locally on default port `1234`. You can
make a request to the API as follows:

    curl -XPOST -H "Content-Type: application/json" -d @test.json http://127.0.0.1:5000/predict_turnover

## Author <a name="authors"></a>

- [Cleyton Farias](mailto:cleytonfarias@outlook.com "e-mail");
