from zenml import step

@step
def deployment_trigger(
    accuracy_valid:float,
    min_accuracy:float = 0.92
):
    return accuracy_valid >= min_accuracy