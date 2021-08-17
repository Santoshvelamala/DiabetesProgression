from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import mlflow
import pandas as pd

app = Flask(__name__)


@app.route('/predict/', methods=['POST'])
def makecalc():
    data = request.get_json()
    data = pd.DataFrame(data)
    prediction = np.array2string(loaded_model.predict(data))
    print ('prediction: ', prediction)
    return jsonify(prediction)

if __name__ == '__main__':
    #modelfile = 'models/final_prediction.pickle'
    #model = p.load(open(modelfile, 'rb'))
    #logged_model = 'runs:/bcaa63346e3f4259b12ab04ff1a23f47/model'
    logged_model = './bcaa63346e3f4259b12ab04ff1a23f47/artifacts/model'
    loaded_model = mlflow.pyfunc.load_model(logged_model)
    app.run(debug=True, host='0.0.0.0', port='8002')