## UCI HAR PROJECT - END-TO-END ML / MLOPS PIPELINE

## ==================================================

An end-to-end machine learning project for human activity recognition using the
UCI Human Activity Recognition Using Smartphones dataset.

The project goes beyond model training by organizing the machine-learning
workflow using **ZenML**, tracking experiments using **MLflow**, evaluating a
classification model, conditionally triggering deployment based on model
performance, and serving the trained model through an MLflow prediction service.



!\[UCI HAR end-to-end pipeline flowchart](images/UCI\_HAR\_End\_to\_End\_Pipeline.png)



\---

## 

## Overview

## \--------

## UCI HAR Dataset

## &#x20;   |

## &#x20;   v

## ZenML Pipeline

## &#x20;   |

## &#x20;   +--> Data Ingestion

## &#x20;   +--> Data Cleaning / Preprocessing

## &#x20;   +--> Train / Validation Split

## &#x20;   +--> Model Training

## &#x20;   +--> Model Evaluation

## &#x20;   +--> Deployment Decision

## &#x20;             |

## &#x20;             +--> If deployment criteria are NOT met:

## &#x20;             |       Stop - do not deploy

## &#x20;             |

## &#x20;             +--> If deployment criteria ARE met:

## &#x20;                     Deploy model with MLflow

## &#x20;                             |

## &#x20;                             v

## &#x20;                     MLflow Model Server

## &#x20;                             |

## &#x20;                             v

## &#x20;                     REST Inference Endpoint

## &#x20;                             |

## &#x20;                             v

## &#x20;                     Prediction Pipeline

## &#x20;                             |

## &#x20;                             v

## &#x20;                     Human Activity Prediction

## 

## 

## ==================================================

## 1\. DATA SOURCE

## ==================================================

## 

## UCI Human Activity Recognition (HAR) Dataset

## \- Smartphone accelerometer and gyroscope measurements

## \- Used to classify human activities

## 

## 

## ==================================================

## 2\. ZENML PIPELINE

## ==================================================

## 

## ZenML is used to orchestrate the end-to-end machine-learning workflow.

## 

## Step 1 - Ingest Data

## \--------------------

## Function:

## &#x20;   ingest\_data\_using\_path

## 

## Purpose:

## \- Load the UCI HAR dataset

## \- Pass the raw data into the pipeline

## 

## 

## &#x20;       |

## &#x20;       v

## 

## 

## Step 2 - Clean / Preprocess Data

## \--------------------------------

## Function:

## &#x20;   clean\_data\_after\_ingestion

## 

## Purpose:

## \- Clean the dataset

## \- Handle missing or invalid data if present

## \- Prepare features and labels for modeling

## 

## 

## &#x20;       |

## &#x20;       v

## 

## 

## Step 3 - Train / Validation Split

## \---------------------------------

## Outputs:

## &#x20;   X\_train

## &#x20;   X\_valid

## &#x20;   y\_train

## &#x20;   y\_valid

## 

## Purpose:

## \- Separate the dataset into training and validation sets

## 

## 

## &#x20;       |

## &#x20;       v

## 

## 

## Step 4 - Train Model

## \--------------------

## Function:

## &#x20;   train\_model\_after\_cleaning

## 

## Example model used:

## &#x20;   Logistic Regression

## 

## Purpose:

## \- Train the machine-learning model using the training data

## 

## 

## &#x20;       |

## &#x20;       v

## 

## 

## Step 5 - Evaluate Model

## \-----------------------

## Function:

## &#x20;   evaluate\_model\_after\_training

## 

## Purpose:

## \- Evaluate the trained model on validation data

## \- Compute model-performance metrics such as:

## &#x20;   - Accuracy

## &#x20;   - Precision

## &#x20;   - Recall

## &#x20;   - F1-score

## &#x20;   - Classification report

## 

## 

## ==================================================

## 3\. MLFLOW EXPERIMENT TRACKING

## ==================================================

## 

## MLflow is used alongside the ZenML pipeline for experiment tracking.

## 

## MLflow records information such as:

## 

## \- Model parameters

## \- Model hyperparameters

## \- Evaluation metrics

## \- Model artifacts

## \- Run metadata

## \- Experiment history

## 

## Conceptually:

## 

## &#x20;   ZenML Pipeline Steps

## &#x20;           |

## &#x20;           +------------------------------+

## &#x20;           |                              |

## &#x20;           v                              v

## &#x20;     Model Training                 Model Evaluation

## &#x20;           |                              |

## &#x20;           +--------------+---------------+

## &#x20;                          |

## &#x20;                          v

## &#x20;                 MLflow Experiment Tracking

## 

## 

## This makes model runs reproducible and allows different experiments

## to be compared.

## 

## 

## ==================================================

## 4\. DEPLOYMENT DECISION

## ==================================================

## 

## After model evaluation:

## 

## &#x20;                   Model Evaluation

## &#x20;                          |

## &#x20;                          v

## &#x20;               Meets deployment criteria?

## &#x20;                   /                \\

## &#x20;                 No                  Yes

## &#x20;                 |                    |

## &#x20;                 v                    v

## &#x20;       Stop / Do not deploy      Deploy Model

## 

## 

## The exact deployment threshold is configurable and can be changed

## depending on the requirements of the project.

## 

## 

## ==================================================

## 5\. MODEL DEPLOYMENT

## ==================================================

## 

## Step 6 - Deploy Model

## \---------------------

## ZenML deployment step:

## &#x20;   mlflow\_model\_deployer\_step

## 

## Purpose:

## \- Use ZenML to coordinate model deployment

## \- Pass the validated model to the MLflow deployer

## 

## 

## &#x20;       |

## &#x20;       v

## 

## 

## Step 7 - MLflow Model Server

## \----------------------------

## Purpose:

## \- Start or reuse an MLflow model-serving service

## \- Load the deployed model

## \- Make the model available for inference

## 

## 

## &#x20;       |

## &#x20;       v

## 

## 

## Step 8 - REST Inference Endpoint

## \--------------------------------

## Example endpoint:

## &#x20;   /invocations

## 

## Purpose:

## \- Allow another application or pipeline step to send data to the model

## \- Return model predictions through an HTTP request / response interface

## 

## 

## ==================================================

## 6\. INFERENCE / PREDICTION PIPELINE

## ==================================================

## 

## New / Test Data

## &#x20;     |

## &#x20;     v

## Preprocess Input Data

## &#x20;     |

## &#x20;     v

## Send Prediction Request

## &#x20;     |

## &#x20;     v

## MLflow REST Endpoint

## &#x20;     |

## &#x20;     v

## Model Inference

## &#x20;     |

## &#x20;     v

## Receive Prediction

## &#x20;     |

## &#x20;     v

## Human Activity Prediction

## 

## 

## Step 1 - Load Test / New Data

## \-----------------------------

## \- Load data that should be classified

## \- Ensure it has the same feature structure expected by the model

## 

## 

## Step 2 - Apply Preprocessing

## \----------------------------

## \- Apply the same preprocessing logic used during training

## 

## 

## Step 3 - Send Prediction Request

## \--------------------------------

## \- Send the input data to the MLflow prediction server

## \- Use a supported request format such as JSON or CSV

## 

## 

## Step 4 - Receive Prediction

## \---------------------------

## \- Read the response returned by the MLflow model server

## 

## 

## Step 5 - Human Activity Prediction

## \----------------------------------

## Example predicted activities may include:

## \- Walking

## \- Walking upstairs

## \- Walking downstairs

## \- Sitting

## \- Standing

## \- Laying

## 

## 

## ==================================================

## 7\. COMPLETE PIPELINE SUMMARY

## ==================================================

## 

## UCI HAR Dataset

## &#x20;   |

## &#x20;   v

## \[ZenML]

## Ingest Data

## &#x20;   |

## &#x20;   v

## Clean / Preprocess

## &#x20;   |

## &#x20;   v

## Train / Validation Split

## &#x20;   |

## &#x20;   v

## Train Model

## &#x20;   |

## &#x20;   +------------------> \[MLflow Experiment Tracking]

## &#x20;   |

## &#x20;   v

## Evaluate Model

## &#x20;   |

## &#x20;   +------------------> \[MLflow Metrics / Run Tracking]

## &#x20;   |

## &#x20;   v

## Deployment Decision

## &#x20;   |

## &#x20;   +---- No ----> Stop

## &#x20;   |

## &#x20;   +---- Yes ---> Deploy Model

## &#x20;                      |

## &#x20;                      v

## &#x20;               MLflow Model Server

## &#x20;                      |

## &#x20;                      v

## &#x20;               REST API Endpoint

## &#x20;                      |

## &#x20;                      v

## &#x20;               Prediction Request

## &#x20;                      |

## &#x20;                      v

## &#x20;               Model Prediction

## &#x20;                      |

## &#x20;                      v

## &#x20;            Human Activity Output

## 

## 

## ==================================================

## 8\. TECHNOLOGIES USED

## ==================================================

## 

## ZenML

## \- Pipeline orchestration

## \- Reproducible ML workflow

## \- Coordination of training, evaluation, and deployment

## 

## MLflow

## \- Experiment tracking

## \- Metrics and artifact logging

## \- Model serving

## \- REST inference endpoint

## 

## scikit-learn

## \- Machine-learning model implementation

## \- Logistic Regression used in the current project

## 

## Pandas / NumPy

## \- Data processing and numerical operations

## 

## Git / GitHub

## \- Version control

## \- Project documentation

## \- Source-code repository

## 

## 

## ==================================================

## 9\. REUSABLE TEMPLATE FOR FUTURE ML PROJECTS

## ==================================================

## 

## The same architecture can be reused for other projects:

## 

## Raw Data

## &#x20;   |

## &#x20;   v

## Data Ingestion

## &#x20;   |

## &#x20;   v

## Data Validation / Cleaning

## &#x20;   |

## &#x20;   v

## Feature Engineering / Preprocessing

## &#x20;   |

## &#x20;   v

## Train / Validation Split

## &#x20;   |

## &#x20;   v

## Model Training

## &#x20;   |

## &#x20;   +----> Experiment Tracking

## &#x20;   |

## &#x20;   v

## Model Evaluation

## &#x20;   |

## &#x20;   v

## Deployment Decision

## &#x20;   |

## &#x20;   +----> Reject / Retrain

## &#x20;   |

## &#x20;   +----> Deploy

## &#x20;             |

## &#x20;             v

## &#x20;        Model Server

## &#x20;             |

## &#x20;             v

## &#x20;        API Endpoint

## &#x20;             |

## &#x20;             v

## &#x20;        Inference Pipeline

## &#x20;             |

## &#x20;             v

## &#x20;        Predictions

## &#x20;             |

## &#x20;             v

## &#x20;        Monitoring / Future Retraining

## 

## 

## This structure separates the major responsibilities of an end-to-end

## ML system and can be adapted to different datasets, models, deployment

## criteria, and inference environments.

## 

