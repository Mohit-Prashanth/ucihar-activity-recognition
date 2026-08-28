from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression, LogisticRegression
import logging
import pandas as pd
import numpy as np
#import torch
#import torch.nn as nn

class ModelStrategy(ABC):

    @abstractmethod
    def train(self, X_train, y_train):
        pass

class LinearRegresssionStrategy(ModelStrategy):

    def train(self, X_train:pd.DataFrame, y_train:np.ndarray):
        linear_regression_object = LinearRegression()
        model = linear_regression_object.fit(X_train, y_train)
        logging.info('Model is trained')
        return model

class LogisticRegresssionStrategy(ModelStrategy):

    def train(self, X_train:pd.DataFrame, y_train:np.ndarray):
        logistic_regression_object = LogisticRegression()
        model = logistic_regression_object.fit(X_train, y_train)
        logging.info('Model is trained')
        return model

#class MLPStrategy(ModelStrategy):
    #def train(self, X_train:pd.DataFrame, y_train:pd.Series):
        