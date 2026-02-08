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

from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file:
            dill.dump(obj, file)
    
    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_models(x_train,y_train,x_test,y_test, models):
    try:
        report = {}
        
        for i in range(len(list(models))):
            model = list(models.values())[i]
            model = model.fit(x_train,y_train)
            y_pred= model.predict(x_test)
            r2_scores = r2_score(y_test,y_pred)
            
            report[list(models.keys())[i]]=r2_scores
            
        return report
        
    except Exception as e:
        raise CustomException(e,sys)