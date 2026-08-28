# Use this file to change which model to train

from zenml import step
from src.model_dev import LinearRegresssionStrategy, LogisticRegresssionStrategy
import pandas as pd
import numpy as np
import mlflow
from sklearn.base import ClassifierMixin
from zenml.client import Client

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def train_model_after_cleaning(
    X_train:pd.DataFrame, 
    y_train:np.ndarray,
    model_name:str
) -> ClassifierMixin:
    
    trained_model = None
    if model_name == 'LinearRegression':
        mlflow.sklearn.autolog()
        trained_model = LinearRegresssionStrategy().train(X_train, y_train)
        return trained_model
    elif model_name == 'LogisticRegression':
        mlflow.sklearn.autolog()
        trained_model = LogisticRegresssionStrategy().train(X_train, y_train)
        return trained_model
    else:
        raise ValueError('Model not supported')