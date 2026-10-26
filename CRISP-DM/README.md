# CRISP-DM project: Telco Customer Churn Prediction

- Dataset: Telco Customer Churn
- Target: Whether a customer churns (Yes or No)
- Goal: Identify customers at high risk of leaving
- Methodology: CRISP-DM
- Project type: Binary classification
- Final outcome: An evaluated churn model plus a simple deployment demonstration

## Dataset

Source: [Kaggle Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

The dataset contains 7,043 customer records and 21 variables.

## Methodology

This project follows the six CRISP-DM phases:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

## Models Evaluated

- Logistic Regression
- Random Forest
- Gradient Boosting

## Final Model

The selected model is Logistic Regression.

The deployment threshold is:

0.40

## Prediction Script

The deployment prediction script is located at:

`CRISP-DM/deployment/predict.py`

Run it from the repository root:

```bash
python3 CRISP-DM/deployment/predict.py```

## Saved Model Artifacts

The saved deployment files are located in:

`CRISP-DM/models/`

Files:

- `telco_preprocessor.joblib` — preprocessing pipeline
- `telco_churn_logistic_model.joblib` — trained Logistic Regression model
- `deployment_config.joblib` — decision threshold configuration

The prediction script loads these files automatically when executed.
