## UCI HAR PROJECT - END-TO-END ML / MLOPS PIPELINE

## ==================================================

An end-to-end machine learning project for human activity recognition using the
UCI Human Activity Recognition Using Smartphones dataset.

The project goes beyond model training by organizing the machine-learning
workflow using **ZenML**, tracking experiments using **MLflow**, evaluating a
classification model, conditionally triggering deployment based on model
performance, and serving the trained model through an MLflow prediction service.



The project uses **ZenML** to orchestrate the machine-learning workflow and **ZenML** for experiment tracking, model deployment, and model serving.



1\. \*\*Data Ingestion\*\*

&#x20;  The UCI Human Activity Recognition dataset is loaded into the ZenML pipeline using `ingest\_data\_using\_path`.



2\. \*\*Data Cleaning and Preprocessing\*\*

&#x20;  The ingested data is cleaned and prepared for modeling using `clean\_data\_after\_ingestion`.



3\. \*\*Train/Validation Split\*\*

&#x20;  The processed dataset is divided into training and validation sets: `X\_train`, `X\_valid`, `y\_train`, and `y\_valid`.



4\. \*\*Model Training\*\*

&#x20;  A classification model is trained using `train\_model\_after\_cleaning`. The current implementation uses Logistic Regression.



5\. \*\*MLflow Experiment Tracking\*\*

&#x20;  Training runs are tracked with MLflow. Model parameters, evaluation metrics, artifacts, and run metadata are recorded for reproducibility and experiment comparison.



6\. \*\*Model Evaluation\*\*

&#x20;  The trained model is evaluated on the validation dataset using `evaluate\_model\_after\_training`. Classification metrics are used to assess model performance.



7\. \*\*Deployment Decision\*\*

&#x20;  The pipeline checks whether the trained model satisfies the configured deployment criteria. If the criteria are not met, deployment is skipped.



8\. \*\*Model Deployment\*\*

&#x20;  If the model satisfies the deployment criteria, ZenML triggers `mlflow\_model\_deployer\_step` to deploy the model through MLflow.



9\. \*\*MLflow Model Server\*\*

&#x20;  MLflow starts or reuses a model-serving service and exposes the deployed model through a prediction endpoint.



10\. \*\*Inference\*\*

&#x20;   New or test data is prepared using the same preprocessing logic used during training and sent to the MLflow `/invocations` endpoint.



11\. \*\*Prediction Output\*\*

&#x20;   The deployed model returns a predicted human-activity class, such as walking, sitting, standing, or laying.



