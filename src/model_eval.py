from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
from sklearn.metrics import (
classification_report,
confusion_matrix,
ConfusionMatrixDisplay,
accuracy_score
)

class EvalStrategy(ABC):

    @abstractmethod
    def eval(
        self,
        y_true:np.ndarray,
        y_pred:np.ndarray        
    ):
        pass

class ClassificationReportStrategy(EvalStrategy):

    def eval(
        self,
        y_true:np.ndarray,
        y_pred:np.ndarray
    ) -> str | dict:

        classification_report_evaluated = classification_report(y_true, y_pred)

        return classification_report_evaluated

class AccuracyScoreStrategy(EvalStrategy):

    def eval(
        self,
        y_true:np.ndarray,
        y_pred:np.ndarray
    ) -> float:

        accuracy_score_evaluated = accuracy_score(y_true, y_pred)

        return accuracy_score_evaluated
        
        