from steps.ingest_data import ingest_data_using_path
from steps.clean_data import clean_data_after_ingestion
from steps.model_train import train_model_after_cleaning
from steps.evaluate import evaluate_model_after_training

from zenml import pipeline

@pipeline(enable_cache=False)
def train_pipeline(data_path:str):
    df = ingest_data_using_path(data_path)
    X_train, X_valid, y_train, y_valid = clean_data_after_ingestion(df)
    model = train_model_after_cleaning(
        X_train, 
        y_train, 
        model_name = 'LogisticRegression'
    )
    report = evaluate_model_after_training(
        X_valid,
        y_valid,
        model,
        report_type = 'Accuracy score'
    ) 

    
