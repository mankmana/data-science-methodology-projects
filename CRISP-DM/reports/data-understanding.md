# CRISP-DM Phase 2: Data Understanding

## 1. Data Source

The dataset used in this project is the Telco Customer Churn dataset.

Source:

[Kaggle: Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

Local file:

`CRISP-DM/data/raw/Telecom Custmer Data Churn.csv`

## 2. Dataset Overview

The dataset contains:

- 7,043 customer records
- 21 variables
- Customer demographic information
- Customer account information
- Subscribed services
- Billing information
- Churn status

Each row represents one telecommunications customer.

## 3. Target Variable

The prediction target is:

`Churn`

Possible values are:

- `Yes` — the customer left the company
- `No` — the customer remained with the company

This is a binary classification problem.

## 4. Initial Findings

The dataset contains 7,043 customer records and 21 variables.

The observed distribution of the target variable is:

- 73.46% of customers did not churn.
- 26.54% of customers churned.

This indicates that the target variable is imbalanced because the number of customers who stayed is substantially larger than the number who churned.

## Data Preparation Completion

The data was cleaned and transformed for machine-learning use.

The `TotalCharges` column was converted from text to numeric format. Invalid values were treated as missing and removed. The `customerID` identifier was excluded, and the `Churn` target was converted into binary values.

Numerical features were imputed and standardized. Categorical features were imputed and one-hot encoded.

The preprocessing was fitted only on the training data and then applied to the test data to avoid data leakage.

## Baseline Model: Logistic Regression

The Logistic Regression model achieved:

- Accuracy: 80.38%
- ROC-AUC: 0.836
- Churn precision: 0.65
- Churn recall: 0.57
- Churn F1-score: 0.61

The model correctly identifies approximately 57% of customers who actually churned. This means it misses some potential churners, so recall may need improvement for a customer-retention use case.

The accuracy is 80.38%, but accuracy alone is not sufficient because the dataset is imbalanced. The ROC-AUC score of 0.836 indicates that the model has reasonably strong ability to distinguish between customers who churn and customers who do not churn.

This is a baseline model. Additional models will be trained and compared before selecting the final model.

## Confusion Matrix Interpretation

The confusion matrix shows that the model correctly predicted 917 customers who did not churn and 214 customers who did churn.

The model incorrectly predicted churn for 116 customers who actually stayed. More importantly, it failed to identify 160 customers who actually churned.

The churn recall is approximately 57.2%, meaning the model identified about 57% of all customers who churned. The remaining churners were false negatives and represent potential missed retention opportunities.

## Random Forest Results

The Random Forest model achieved an accuracy of 79.03% and a ROC-AUC score of 0.813.

For the churn class, the model achieved:

- Precision: 0.64
- Recall: 0.49
- F1-score: 0.56

Compared with Logistic Regression, Random Forest performed worse in accuracy, ROC-AUC, recall, and F1-score.

The Random Forest model identified only 49% of customers who actually churned. Since identifying potential churners is an important business objective, Logistic Regression is currently the better-performing model.


## Gradient Boosting Results

The Gradient Boosting model achieved:

- Accuracy: 79.60%
- ROC-AUC: 0.839
- Churn precision: 0.64
- Churn recall: 0.53
- Churn F1-score: 0.58

The model achieved the highest ROC-AUC score among the three tested models, indicating strong ability to distinguish between customers who churn and customers who do not churn.

However, its churn recall was 53%, which was lower than Logistic Regression's recall of 57%. Since identifying potential churners is an important business objective, Logistic Regression currently appears more suitable for the retention use case.

The Gradient Boosting model remains a strong alternative because it produced the highest ROC-AUC score.


## Model Comparison

Three classification models were evaluated using the same training and testing data.

Logistic Regression achieved the highest accuracy, churn recall, and churn F1-score. Gradient Boosting achieved the highest ROC-AUC score, indicating slightly stronger overall ranking ability.

Because the business goal is to identify customers who may churn, churn recall is especially important. Logistic Regression identified 57% of actual churners, compared with 53% for Gradient Boosting and 49% for Random Forest.

Logistic Regression is currently the preferred model for this project, although threshold tuning and additional evaluation will be performed before making the final decision.

## Confusion Matrix Comparison

Logistic Regression produced the highest number of true positives, correctly identifying 214 customers who churned. It also produced the fewest false negatives, missing 160 actual churners.

Random Forest had the fewest false positives, but it missed 189 actual churners. Gradient Boosting missed 176 actual churners.

For this retention-focused project, false negatives are particularly important because they represent customers who churned without being identified by the model. Therefore, Logistic Regression is currently the preferred model.

## Threshold Selection

The default threshold of 0.50 produced a churn recall of 57.2%. Lowering the threshold to 0.40 increased recall to 68.4% and improved the F1-score from 0.608 to 0.627.

The 0.40 threshold is preferred for this project because the business wants to identify more potential churners. The trade-off is lower precision, meaning that more customers who do not churn may be contacted.

The threshold should ultimately be adjusted according to the financial cost of missed churners compared with unnecessary retention efforts.

## Final Model Evaluation

The Logistic Regression model was evaluated using a decision threshold of 0.40.

This threshold was selected because it provided the highest F1-score among the tested thresholds while maintaining strong churn recall.

The threshold of 0.40 provides a balance between identifying potential churners and limiting unnecessary retention offers. A threshold of 0.30 produced higher recall but also lower precision and more false-positive predictions.

The final model and threshold used for deployment are:

- Model: Logistic Regression
- Decision threshold: 0.40
