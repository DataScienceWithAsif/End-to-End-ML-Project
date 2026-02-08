import os
import sys
import pandas as pd
import numpy as np 
import dill
from src.exception import CustomException

from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file:
            dill.dump(obj, file)
    
    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_models(x_train,y_train,x_test,y_test, models, params):
    try:
        report = {}
        
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            
            gs=GridSearchCV(model, param, cv=3)
            gs.fit(x_train,y_train)
            
            model.set_params(**gs.best_params_)
            model = model.fit(x_train,y_train)
            y_pred= model.predict(x_test)
            r2_scores = r2_score(y_test,y_pred)
            
            report[list(models.keys())[i]]=r2_scores
            
        return report
        
    except Exception as e:
        raise CustomException(e,sys)
    
def return_model_params():
    params = {
        "Linear_Regression": {},
        "Gradient_Boosting": {
            "learning_rate":[.1,.01,.05,.001],
            "subsample":[.6,.7,.75,.8,.85,.9],
            "max_features":[.1,.2,.5,.9,1.0],
            "n_estimators":[8,16,32,64,128,256]
            },
        "KNRegressor":{
            "n_neighbors":[5,7,9,11],
            "weights":["uniform","distance"]
            },
        "Decision_Tree":{
            "criterion":["squared_error","friedman_mse","absolute_error","poisson"],
            "max_features":["sqrt","log2"]
            },
        "Random_forest_regressor":{
            "n_estimators":[8,16,32,64,128,256],
            "max_features":["sqrt","log2",None]
            },
        "AdaBoostRegressor":{
          "learning_rate":[.1,.01,.05,.001],
          "loss":["linear","square","exponential"],
          "n_estimators":[8,16,32,64,128,256]  
        }
    }
    return params