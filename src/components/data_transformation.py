import os
import sys
import numpy as np
import os.path
import pandas as pd
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")
    
class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        
    def get_preprocessor_obj(self):
        try:
            num_columns = ["reading_score","writing_score"]
            cat_columns =[
            "gender",
            "race_ethnicity",
            "parental_level_of_education",
            "lunch",
            "test_preparation_course"
            ]
        
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("encoder",OneHotEncoder())
                ]
            )
            logging.info("Cat and numerical pipelines created")
        
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, num_columns),
                    ("cat_pipeline", cat_pipeline, cat_columns)
                ]
            )
        
            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_tranformation(self,train_data,test_data):
        try:
            train_df=pd.read_csv(train_data)
            test_df=pd.read_csv(test_data)
            logging.info("Reading train and test data complete")
            
            logging.info("obtaining preprocessor object")
            preprocessor = self.get_preprocessor_obj()
            
            target_col = "math_score"
            x_train = train_df.drop(columns=[target_col], axis=1)
            y_train = train_df[target_col]
            
            x_test = test_df.drop(columns=[target_col], axis=1)
            y_test = test_df[target_col]
            
            logging.info("Applying preprocessing on x_train and x_test and then concating with target column")
            x_train_arr=preprocessor.fit_transform(x_train)
            x_test_arr =preprocessor.transform(x_test)
            
            train_arr =np.c_[
                x_train_arr, np.array(y_train)
            ]
            test_arr = np.c_[
                x_test_arr, np.array(y_test)
            ]
            
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessor
            )
            
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
            
            
        except Exception as e:
            raise CustomException(e,sys)
        