from zenml import step
import pandas as pd
import logging
from src.data_ingestion import IngestData

@step
def ingest_data_using_path(data_path:str) -> pd.DataFrame:
    #ingest_data_object = IngestData(data_path)
    #print(ingest_data_object.data_path)
    ingest_data_object = IngestData(data_path)
    df = ingest_data_object.get_data()
    return df