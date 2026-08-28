from zenml import step
import pandas as pd
import numpy as np
import mlflow
from src.model_eval import ClassificationReportStrategy, AccuracyScoreStrategy
from sklearn.base import ClassifierMixin
from zenml.client import Client

experiment_tracker = Client().active_stack.experiment_tracker

@step(experiment_tracker=experiment_tracker.name)
def evaluate_model_after_training(
    X_test:pd.DataFrame,
    y_test:np.ndarray,
    model:ClassifierMixin,
    report_type:str
) -> str | dict | float:
    
    y_pred = model.predict(X_test)

    if report_type == 'Classification report':
        report = ClassificationReportStrategy().eval(
            y_test,
            y_pred
        )
        mlflow.log_text(report, 'Classification Report.txt')
        
    elif report_type == 'Accuracy score':
        report = AccuracyScoreStrategy().eval(
            y_test,
            y_pred
        )
        mlflow.log_metric('Accuracy score', report) 
    return report

    

    