from flask import Flask,jsonify,request
import numpy as np
import util

app = Flask(__name__)

@app.route('/get_column_names',methods=['GET'])
def get_column_names():
    response = jsonify({'Columns' : util.get_data_columns()})
    return response


@app.route('/predict_hdisease', methods=['POST'])
def predict_hdisease():

    Age = float(request.form['age'])
    Sex = float(request.form['sex'])
    Chest_Pain_Type = float(request.form['cp'])
    Resting_Blood_Sugar = float(request.form['trestbps'])
    Cholestoral = float(request.form['chol'])
    Fasting_Blood_Sugar = float(request.form['fbs'])
    Resting_Electrocardiographic_Results = float(request.form['restecg'])
    Maximum_Heart_Rate_Achieved = float(request.form['thalach'])
    Exercise_Induced_Angina = float(request.form['exang'])
    Oldpeak = float(request.form['oldpeak'])
    Heart_Slope = float(request.form['slope'])
    Major_Vessels_Colored = float(request.form['ca'])
    Thalium_Stress_Result = float(request.form['thal'])

    response = jsonify({"Predict_Heart_Disease" : util.predict_hdisease(Age,Sex,Chest_Pain_Type,Resting_Blood_Sugar ,Cholestoral,Fasting_Blood_Sugar,
                                                               Resting_Electrocardiographic_Results,Maximum_Heart_Rate_Achieved,Exercise_Induced_Angina,
                                                               Oldpeak ,Heart_Slope, Major_Vessels_Colored,Thalium_Stress_Result)})

    response.headers.add('Access-Control-Allow-Origin' , '*')
    
    return response


util.load_artifacts()
app.run()


