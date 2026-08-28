''' Model deployment steps
✓ pipeline runs
✓ model logged in MLflow
✓ accuracy calculated
✓ deployment_trigger returns True
✓ MLflow deployer exists in active stack
✓ MLflow experiment tracker exists in active stack
✓ MLflow deployment service starts
✓ prediction URL exists
✓ new data sent to service
✓ prediction returned successfully
'''


from zenml import pipeline
from zenml.config import DockerSettings
from zenml.integrations.constants import MLFLOW
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step

from steps.ingest_data import ingest_data_using_path
from steps.clean_data import clean_data_after_ingestion
from steps.model_train import train_model_after_cleaning
from steps.evaluate import evaluate_model_after_training
from steps.trigger_deployment_after_validation import deployment_trigger

docker_settings = DockerSettings(required_integrations=[MLFLOW])

@pipeline(
    enable_cache = False,
    settings = {
        'docker':docker_settings
    }
)

def continuous_deployment_pipeline(
    data_path:str,
    min_accuracy:float = 0.92,
    workers:int = 1,
    timeout:int = DEFAULT_SERVICE_START_STOP_TIMEOUT    
):
    
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
    deploy_decision = deployment_trigger(
        accuracy_valid = report,
        min_accuracy = min_accuracy
    )
    mlflow_model_deployer_step(
        model = model,
        deploy_decision = deploy_decision, 
        timeout = timeout,
        workers = workers
    )
