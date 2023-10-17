import pickle
import json
import numpy as np

_data_columns = None
_model = None

def predict_hdisease(Age, Sex, Chest_Pain_Type, Resting_Blood_Sugar, Cholestoral, Fasting_Blood_Sugar, Resting_Electrocardiographic_Results,
                     Maximum_Heart_Rate_Achieved, Exercise_Induced_Angina, Oldpeak, Heart_Slope, Major_Vessels_Colored,  Thalium_Stress_Result):

    x = np.zeros(len(_data_columns))
    
    x[0] = Age 
    x[1] = Sex
    x[2] = Chest_Pain_Type
    x[3] = Resting_Blood_Sugar
    x[4] = Cholestoral
    x[5] = Fasting_Blood_Sugar
    x[6] = Resting_Electrocardiographic_Results
    x[7] = Maximum_Heart_Rate_Achieved
    x[8] = Exercise_Induced_Angina
    x[9] = Oldpeak
    x[10] = Heart_Slope
    x[11] = Major_Vessels_Colored
    x[12] = Thalium_Stress_Result
    
    return _model.predict([x])[0]

def load_artifacts():
    print("Loading Artifacts information.....")
    global _data_columns
    global _model

    with open("C:/Users/anush/Downloads/Heart_Disease_Prediction/cols.json","r") as f:
        _data_columns = json.load(f)["data_columns"]

    if _model is None:
        with open("C:/Users/anush/Downloads/Heart_Disease_Prediction/heartdisease.pickle","rb") as f:
            _model = pickle.load(f)

def get_data_columns():
    return _data_columns

load_artifacts()
print(get_data_columns())
print(predict_hdisease(37, 1, 2, 130, 250, 0, 1, 187, 0, 3.5, 0, 0, 2))
