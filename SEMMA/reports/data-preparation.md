# SEMMA Data Preparation

This document describes the data preparation performed during the SEMMA Modify phase.

## Dataset

The Bank Marketing dataset contains customer demographic, financial, and campaign information. The target variable is `deposit`.

- `yes`: Customer subscribed to a term deposit
- `no`: Customer did not subscribe

The data was divided into:

- Development sample: 8,929 records
- Holdout sample: 2,233 records



## Planned Preparation

- Check for missing values
- Check for duplicate records
- Encode categorical variables
- Scale numerical variables when appropriate
- Convert the target variable into binary form
- Separate input features from the target
- Prepare the data for modeling


## Findings from Exploration

- No missing values were found.
- No duplicate records were found.
- The target classes are relatively balanced:
  - `no`: 52.62%
  - `yes`: 47.38%
- Numerical variables contain outliers.
- `balance` is strongly right-skewed.
- `pdays` contains many `-1` values, indicating that the customer was not previously contacted.
- `previous` contains many zero values.
- Categorical variables require encoding before modeling.

## Planned Data Preparation

- Convert the target variable into binary values.
- Separate predictor variables from the target.
- Encode categorical variables using one-hot encoding.
- Scale numerical variables when required by the model.
- Review outliers without automatically removing valid customer records.
- Decide how to handle the special `pdays = -1` value.
- Review `duration` because it is measured during the customer contact and may not be available before a campaign call.

### Encoding and Scaling

Categorical variables are converted into numerical indicator columns using one-hot encoding. Numerical variables are standardized so that they have comparable scales. The preprocessing steps are fitted only on the development sample and then applied to the holdout sample.

## Completed Preparation

The target variable was converted into binary values, with `no` represented as `0` and `yes` represented as `1`.

The predictor variables were separated from the target. Categorical variables were one-hot encoded, and numerical variables were standardized.

The original 16 predictor columns expanded to 51 prepared features after one-hot encoding.

- Prepared development data: 8,929 records and 51 features
- Prepared holdout data: 2,233 records and 51 features

The preprocessing transformer was fitted only on the development data and then applied to the holdout data.

## SEMMA Model Phase

Three classification models will be trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest

The models will use the prepared development data and will be evaluated later using the holdout data.

### Model Comparison

Random Forest performed best on the holdout sample. It achieved an accuracy of 0.858, recall of 0.888, F1-score of 0.855, and ROC-AUC of 0.920. It was selected as the preferred model because it provided the strongest overall performance, especially for identifying customers who subscribed to a term deposit.

Logistic Regression performed moderately well, while the Decision Tree had the lowest performance among the three models.

### Confusion Matrix Interpretation

The Random Forest confusion matrix contains 976 true negatives, 199 false positives, 119 false negatives, and 939 true positives. It produced fewer false negatives than Logistic Regression and Decision Tree, which explains its higher recall for customers who subscribed to a term deposit.

The Random Forest model was selected as the preferred model because it achieved the strongest overall assessment results.
