import sys
from flask import Flask, request
from joblib import load
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route("/predict_turnover", methods=["POST"])
def predict():
    # catching json:
    json_ = request.get_json()
    # convert to DF:
    df = pd.DataFrame(json_) 
    # predicting accumulated turnover:
    # input:
    input_features=['Amount', 'age',
                    'turnover_accum_lag_1',
                    'turnover_accum_lag_2',
                    'turnover_accum_lag_3',
                    'turnover_accum_lag_4',
                    'turnover_accum_lag_5']    
    # outcomes:
    ys = ['turnover_accum_30', 'turnover_accum_45',
          'turnover_accum_60', 'turnover_accum_90']
    ys_pred = []    
    # loop to predict:
    for outcome in ys:
        newcol = outcome+"_pred"
        ys_pred.append(newcol)
        df[newcol] = models[outcome].predict(df[input_features])
    # justando para termos estimações monotonicas:
    df["turnover_accum_45_pred"] = df.apply(lambda x: np.max([x["turnover_accum_30_pred"], x["turnover_accum_45_pred"]]), axis=1)
    df["turnover_accum_60_pred"] = df.apply(lambda x: np.max([x["turnover_accum_45_pred"], x["turnover_accum_60_pred"]]), axis=1)
    df["turnover_accum_90_pred"] = df.apply(lambda x: np.max([x["turnover_accum_60_pred"], x["turnover_accum_90_pred"]]), axis=1)    
    return df[["Username"]+ys_pred].to_json(orient="records")


if __name__ == '__main__':
    # If you don't provide any port the port will be set to 500
    try:
        port = int(sys.argv[1])
    except:
        port = 1234    
    # loading model:
    models = load("models.joblib")
    # running debug mode:
    app.run(port=port, debug=True)


