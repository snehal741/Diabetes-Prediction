# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 17:25:40 2021

@author: Snehal
"""
from flask import render_template, Flask, request, jsonify, url_for
import pickle
import numpy

app = Flask(__name__)

model = pickle.load(open('Diabetes.pkl', 'rb'))


@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')





@app.route('/predict', methods=['POST'])
def predict():
    print('predicting')
    int_features = []
    print(request.form)
    for x in request.form.values():
        # if x.keys() == 'BMI' or x.key == 'dpf':
        #     int_features.append(float(x.value))
        # else:
        int_features.append(float(x))
    final_features = [numpy.array(int_features)]
    prediction = model.predict(final_features)
    print(prediction)
    if prediction == 1:
        print("returning 1")
        return render_template('index.html', prediction_text = "You have Diabetes")
    else:
        print("returning 0")
        return render_template('index.html', prediction_text = "You do not have Diabetes")

if __name__ == '__main__':
    app.run()