from zenml import step
from zenml.integrations.mlflow.services import MLFlowDeploymentService
import pandas as pd
import numpy as np
import requests
import logging
import json

@step
def predictor(
    service,
    data:dict
):
    logging.info(f"Service URL: {service.prediction_url}")
    response = requests.post(
        url = service.prediction_url,
        json = data
    )

    print("Response: ", response)
    print("Status code:", response.status_code)
    print("Content type:", response.headers.get("Content-Type"))
    #print("Response text:", response.text)
    
    prediction = response.json()

    print("Prediction type:", type(prediction))

    return prediction
    