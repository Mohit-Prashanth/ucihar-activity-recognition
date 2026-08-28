from zenml import pipeline
from steps.check_existing_service import get_existing_service
from steps.prediction_after_deployment import predictor
from steps.prepare_data_for_inference import load_data_after_deployment
import logging

@pipeline(enable_cache = False)
def inference_pipeline(
    data_path
):
    payload = load_data_after_deployment(
        data_path
    )
    logging.info("Returned payload successfully")
    
    service = get_existing_service(
        pipeline_name = 'continuous_deployment_pipeline',
        pipeline_step_name = 'mlflow_model_deployer_step',
        model_name = 'model'
    )
    
    prediction = predictor(
        service = service,
        data = payload
    )



    
    