# Prepare test data before sending the data to the service for prediction

from zenml import step
from src.data_ingestion import IngestData
from src.data_transformation import DataTransformation, DataEncodeStrategy, SplitXYStrategy
import pandas as pd
import numpy as np
import logging

@step
def load_data_after_deployment(
    data_path:str
) -> dict:
    data = IngestData(data_path).get_data()
    X, y = DataTransformation(
        data = data,
        strategy = SplitXYStrategy()
    ).handle_data()
    y = DataTransformation(
        data = y,
        strategy = DataEncodeStrategy()
    ).handle_data()

    logging.info(f"Type of data: {type(X)}, {type(y)}")

    #X = X.to_json(orient='split')

    payload = {
        'dataframe_split':{
            'columns':X.columns.tolist(),
            'data':X.values.tolist()
        }
    }
    return payload
    
    
