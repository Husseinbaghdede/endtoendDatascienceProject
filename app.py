from flask import Flask,render_template,request
import os 
import numpy as np 
import pandas as pd  
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)


@app.route('/',methods=['GET']) ## route display the home page
def homepage():
    return render_template("index.html")

@app.route("/train",methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful"

@app.route("/predict",methods=['POST','GET'])
def index():
    if request.method == 'POST':
        try:
            input_data = [
            float(request.form['fixed_acidity']),
            float(request.form['volatile_acidity']),
            float(request.form['citric_acid']),
            float(request.form['residual_sugar']),
            float(request.form['chlorides']),
            float(request.form['free_sulfur_dioxide']),
            float(request.form['total_sulfur_dioxide']),
            float(request.form['density']),
            float(request.form['pH']),
            float(request.form['sulphates']),
            float(request.form['alcohol'])
        ]

            data = np.array(data).reshape(1,11)
            predict = obj.predict(data)

            return render_template('results.html',prediction=str(predict))
        except Exception as e:
            return "something is wrong"
    else:
        return render_template("index.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)


