#clean_data.py

from zenml import step
from src.data_transformation import DataTransformation, DataDivideStrategy, DataEncodeStrategy
import pandas as pd
import numpy as np
from typing import Tuple
from typing_extensions import Annotated

@step
def clean_data_after_ingestion(df:pd.DataFrame) -> Tuple[
    Annotated[pd.DataFrame, 'X_train'],
    Annotated[pd.DataFrame, 'X_valid'],
    Annotated[np.ndarray, 'y_train'],
    Annotated[np.ndarray, 'y_valid'],
]:
    #df = DataTransformation(df, DropNaStrategy()).handle_data()
    X_train, X_valid, y_train, y_valid = DataTransformation(df, DataDivideStrategy()).handle_data()
    y_train = DataTransformation(y_train, DataEncodeStrategy()).handle_data()
    y_valid = DataTransformation(y_valid, DataEncodeStrategy()).handle_data()
    return X_train, X_valid, y_train, y_valid
