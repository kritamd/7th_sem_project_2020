import os
import joblib

config={
    'heart':{
        'LogisticRegression':'production/Logistic_regression_model.pkl',
        'scalar_file':'production/standard_scalar.pkl'
    }

}

dir=os.path.dirname(__file__)

def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir,filepath)):
        return joblib.load(os.path.join(dir,filepath))
    return None

def GetStandardScalerForHeart():
    return GetJobLibFile(config['heart']['scalar_file'])

def GetClassifierForHeart():
    return GetJobLibFile(config['heart']['LogisticRegression'])