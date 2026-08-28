from zenml.steps import BaseParameters

class ModelConfig(BaseParameters):
    """
    Model configuration
    """
    model_name:str = "LinearRegression"