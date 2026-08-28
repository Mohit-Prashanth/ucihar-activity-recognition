from zenml import step
from typing import cast
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import MLFlowModelDeployer
from zenml.integrations.mlflow.services import MLFlowDeploymentService
import logging
from pipelines.deployment_pipeline import continuous_deployment_pipeline

@step
def get_existing_service(
    pipeline_name,
    pipeline_step_name,
    model_name
) -> MLFlowDeploymentService:
    mlflow_model_deployer_component = MLFlowModelDeployer.get_active_model_deployer()
    logging.info(f"Current configured model deployer: {mlflow_model_deployer_component}")

    existing_services = mlflow_model_deployer_component.find_model_server(
        pipeline_name = pipeline_name,
        pipeline_step_name = pipeline_step_name,
        model_name = model_name
    )

    logging.info(f"Existing service: {existing_services}")

    if not existing_services:
        raise RuntimeError("No running model service found")
    
    logging.info("Service available, no need to deploy model again")
    logging.info(f"Existing services: {existing_services[0]}")
    service = cast(MLFlowDeploymentService, existing_services[0])

    if not service.is_running:
        service.start(timeout=60)
    
    #logging.info(f"Type of service: {type(service)}")
    #logging.info(f"Service URL: {service.prediction_url}")
    return service

        

    
    