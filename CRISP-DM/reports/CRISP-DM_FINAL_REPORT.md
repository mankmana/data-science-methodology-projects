# CRISP-DM Final Report: Telco Customer Churn Prediction

## Executive Summary

This project developed a machine-learning solution to identify telecommunications customers who may churn.

The project followed all six CRISP-DM phases:

1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modeling
5. Evaluation
6. Deployment

Three classification models were evaluated. Logistic Regression was selected as the final model because it provided the strongest churn recall and F1-score while remaining interpretable.

The final deployment threshold is 0.40.

## 1. Business Understanding

### Business Problem

Telecommunications companies lose revenue when customers cancel their services. Retaining existing customers is generally less expensive than acquiring new customers.

The company needs a method to identify customers who may be likely to leave.

### Business Objective

Identify high-risk customers early so the company can take retention actions such as:

- Personalized offers
- Contract upgrades
- Technical support
- Customer-service follow-ups

### Data Science Objective

Build a binary classification model that predicts whether a customer will churn.

The target variable is:

- `Churn = Yes`
- `Churn = No`

### Business Questions

This project investigates:

1. Which customer characteristics are associated with churn?
2. Which contract types and services are linked to higher churn?
3. Can churn be predicted using customer information?
4. Which customers should receive retention attention?

### Success Criteria

The project is successful if it:

- Identifies meaningful churn-related patterns.
- Produces useful churn-risk predictions.
- Helps prioritize retention resources.
- Provides explainable results.
- Documents limitations and ethical risks.

## 2. Data Understanding

### Dataset Source

[Kaggle Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### Dataset Description

The dataset contains:

- 7,043 customer records
- 21 variables
- Demographic information
- Account information
- Services used
- Billing information
- Churn status

Each row represents one telecommunications customer.

### Target Distribution

The target variable distribution was:

- 73.46% did not churn
- 26.54% churned

The target variable is therefore imbalanced.

### Data Quality Findings

The `TotalCharges` column was initially stored as an object rather than a numeric column. After removing spaces and converting the values to numeric format, invalid values became missing values.

Eleven records with invalid or missing `TotalCharges` values were removed.

The `customerID` column was identified as an identifier and excluded from modeling.

## 3. Data Preparation

The following preparation steps were performed:

1. Removed spaces from column names.
2. Removed spaces from `TotalCharges` values.
3. Converted `TotalCharges` to numeric.
4. Removed 11 invalid records.
5. Removed `customerID`.
6. Converted `Churn` into binary values:
   - `No = 0`
   - `Yes = 1`
7. Split the data into training and testing sets.
8. Used stratification to preserve the churn distribution.
9. Imputed missing values.
10. Standardized numerical variables.
11. One-hot encoded categorical variables.

The final data split was:

- Training set: 5,625 records
- Testing set: 1,407 records
- Input features: 19

The preprocessing pipeline was fitted only on the training data to prevent data leakage.

## 4. Modeling

Three classification models were trained:

- Logistic Regression
- Random Forest
- Gradient Boosting

All models used the same prepared training and testing data.

## 5. Evaluation

### Model Comparison

| Model | Accuracy | ROC-AUC | Churn Precision | Churn Recall | Churn F1-score |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.804 | 0.836 | 0.65 | 0.57 | 0.61 |
| Random Forest | 0.790 | 0.813 | 0.64 | 0.49 | 0.56 |
| Gradient Boosting | 0.796 | 0.839 | 0.64 | 0.53 | 0.58 |

Gradient Boosting achieved the highest ROC-AUC score. However, Logistic Regression achieved the highest churn recall and F1-score.

Since the business objective is to identify potential churners, churn recall is especially important.

### Confusion Matrix Analysis

Using the default threshold of 0.50:

- Logistic Regression correctly identified 214 churners and missed 160.
- Random Forest correctly identified 185 churners and missed 189.
- Gradient Boosting correctly identified 198 churners and missed 176.

Logistic Regression produced the fewest false negatives.

### Threshold Tuning

| Threshold | Precision | Recall | F1-score |
|---:|---:|---:|---:|
| 0.30 | 0.511 | 0.759 | 0.611 |
| 0.40 | 0.579 | 0.684 | 0.627 |
| 0.50 | 0.648 | 0.572 | 0.608 |
| 0.60 | 0.679 | 0.385 | 0.491 |

A threshold of 0.40 was selected because it produced the highest F1-score while maintaining strong churn recall.

### Final Model

The final selected model is:

- Model: Logistic Regression
- Decision threshold: 0.40

The threshold represents a business trade-off. A lower threshold identifies more potential churners but creates more false-positive retention opportunities.

## 6. Deployment

The deployment implementation is located at:

```text
CRISP-DM/deployment/predict.py```

The saved model artifacts are located in:

```text
CRISP-DM/models/
```

The deployment uses:

- `telco_preprocessor.joblib` — preprocessing pipeline
- `telco_churn_logistic_model.joblib` — trained Logistic Regression model
- `deployment_config.joblib` — decision threshold configuration

Example output:

```text
Churn probability: 29.06%
Prediction: Likely to stay
Decision threshold: 0.4
```

Because the predicted probability was below 0.40, the example customer was classified as likely to stay.

## 7. Limitations

- The data is historical and may not represent current customer behavior.
- The model does not prove that any variable causes churn.
- The dataset may not include important factors such as competitor pricing or customer sentiment.
- False positives may result in unnecessary retention costs.
- False negatives may result in missed retention opportunities.
- Model performance should be monitored after deployment.
- Customer predictions should support human decisions rather than automatically determine customer treatment.

## 8. Ethical Considerations

Customer data should be handled responsibly.

The project avoids using customer identifiers as predictive features. Model results should be reviewed for unfair performance differences across customer groups.

Predictions should not be used to deny service or unfairly penalize customers.

The model should be used to support retention decisions, not to make automatic decisions without human review.

## 9. Reproducibility

The complete project includes:

- Google Colab notebook
- Dataset documentation
- Analysis reports
- Figures
- Saved model artifacts
- Deployment script
- GitHub repository documentation

The main notebook is located in:

```text
CRISP-DM/notebooks/
```

The prediction script is located in:

```text
CRISP-DM/deployment/predict.py
```

The model artifacts are located in:

```text
CRISP-DM/models/
```

## 10. Conclusion

This project demonstrated a complete CRISP-DM workflow for telecommunications customer churn prediction.

Logistic Regression was selected as the final model because it provided the best balance of interpretability, churn recall, and F1-score. A 0.40 decision threshold was chosen to identify potential churners while maintaining a reasonable balance with precision.

The deployed prediction script successfully loaded the saved model artifacts and generated a churn prediction for a new customer.

## References

- [Kaggle Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Google Colab project notebook
- Scikit-learn documentation
