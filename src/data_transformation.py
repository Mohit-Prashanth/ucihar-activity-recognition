#data_transformation.py

import logging
from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

#abstract class
class DataStrategy(ABC):

    @abstractmethod
    def handle_data(self, data:pd.DataFrame) -> pd.DataFrame | pd.Series | np.ndarray:
        pass

#subclass
class DropNaStrategy(DataStrategy):

    def handle_data(self, data:pd.DataFrame) -> pd.DataFrame | pd.Series:
        df = data.dropna()
        return df

class DataDivideStrategy(DataStrategy):

    def handle_data(self, data:pd.DataFrame) -> pd.DataFrame | pd.Series:
        X = data.drop(['subject','Activity'], axis=1)
        y = data['Activity']
        X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.2)
        return X_train, X_valid, y_train, y_valid

class SplitXYStrategy(DataStrategy):

    def handle_data(self, data:pd.DataFrame) -> pd.DataFrame | pd.Series:
        X = data.drop(['subject','Activity'], axis=1)
        y = data['Activity']
        return X, y

class DataEncodeStrategy(DataStrategy):
    
    def handle_data(self, data:pd.DataFrame) -> np.ndarray:
        encoder = preprocessing.LabelEncoder()
        encoder.fit(data)
        data_encoded = encoder.transform(data)
        return data_encoded

#Wrap the strategy subclass using another class
class DataTransformation:

    def __init__(self, data:pd.DataFrame, strategy:DataStrategy):
        self.data = data
        self.strategy = strategy

    def handle_data(self) -> pd.DataFrame | pd.Series:
        return self.strategy.handle_data(self.data)
