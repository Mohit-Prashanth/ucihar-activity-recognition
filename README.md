## UCI HAR PROJECT - END-TO-END ML / MLOPS PIPELINE

## ==================================================

An end-to-end machine learning project for human activity recognition using the
UCI Human Activity Recognition Using Smartphones dataset.

The project goes beyond model training by organizing the machine-learning
workflow using **ZenML**, tracking experiments using **MLflow**, evaluating a
classification model, conditionally triggering deployment based on model
performance, and serving the trained model through an MLflow prediction service.





&#x20;                UCI HAR Dataset

&#x20;                      |

&#x20;                      v

&#x20;             +------------------+

&#x20;             |   Data Ingestion |

&#x20;             |      ZenML       |

&#x20;             +------------------+

&#x20;                      |

&#x20;                      v

&#x20;             +------------------+

&#x20;             | Data Cleaning \&  |

&#x20;             |  Preprocessing   |

&#x20;             +------------------+

&#x20;                      |

&#x20;                      v

&#x20;             +------------------+

&#x20;             | Train / Validation|

&#x20;             |      Split       |

&#x20;             +------------------+

&#x20;                      |

&#x20;                      v

&#x20;             +------------------+

&#x20;             |   Model Training |

&#x20;             | Logistic Regression

&#x20;             +------------------+

&#x20;                      |

&#x20;                      +----------------------+

&#x20;                      |                      |

&#x20;                      |                      v

&#x20;                      |            +----------------------+

&#x20;                      |            | MLflow Experiment    |

&#x20;                      |            | Tracking             |

&#x20;                      |            |                      |

&#x20;                      |            | - Parameters         |

&#x20;                      |            | - Metrics            |

&#x20;                      |            | - Model artifacts    |

&#x20;                      |            | - Run metadata       |

&#x20;                      |            +----------------------+

&#x20;                      |

&#x20;                      v

&#x20;             +------------------+

&#x20;             | Model Evaluation |

&#x20;             +------------------+

&#x20;                      |

&#x20;                      v

&#x20;             +-----------------------+

&#x20;             | Meets Deployment      |

&#x20;             | Criteria?             |

&#x20;             +-----------------------+

&#x20;                 |               |

&#x20;                No              Yes

&#x20;                 |               |

&#x20;                 v               v

&#x20;         +---------------+   +----------------------+

&#x20;         | Stop / Do Not |   | Deploy Model         |

&#x20;         |    Deploy     |   | ZenML + MLflow       |

&#x20;         +---------------+   +----------------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                             +----------------------+

&#x20;                             | MLflow Model Server  |

&#x20;                             +----------------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                             +----------------------+

&#x20;                             | REST Prediction      |

&#x20;                             | Endpoint             |

&#x20;                             | /invocations         |

&#x20;                             +----------------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                             +----------------------+

&#x20;                             | Load New / Test Data |

&#x20;                             +----------------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                             +----------------------+

&#x20;                             | Apply Preprocessing  |

&#x20;                             +----------------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                             +----------------------+

&#x20;                             | Send Prediction      |

&#x20;                             | Request              |

&#x20;                             +----------------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                             +----------------------+

&#x20;                             | Receive Prediction   |

&#x20;                             +----------------------+

&#x20;                                     |

&#x20;                                     v

&#x20;                             +----------------------+

&#x20;                             | Human Activity       |

&#x20;                             | Prediction           |

&#x20;                             +----------------------+

