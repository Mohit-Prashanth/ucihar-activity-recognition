# UCI HAR Activity Recognition — MLOps Pipeline

An end-to-end machine learning project for human activity recognition using the
UCI Human Activity Recognition Using Smartphones dataset.

The project goes beyond model training by organizing the machine-learning
workflow using **ZenML**, tracking experiments using **MLflow**, evaluating a
classification model, conditionally triggering deployment based on model
performance, and serving the trained model through an MLflow prediction service.



\---



## Project Overview

The objective of this project is to build a reproducible machine-learning
pipeline for classifying human activities from smartphone sensor measurements.

The project demonstrates the progression from:


data ingestion
      ↓
data preprocessing
      ↓
model training
      ↓
model evaluation
      ↓
deployment decision
      ↓
model deployment
      ↓
inference

