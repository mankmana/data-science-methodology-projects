# SEMMA Bank Marketing Subscription Prediction

## Project Context and Business Objective

The goal of this project is to predict whether a bank customer will subscribe to a term deposit after a marketing campaign.

The target variable is `deposit`:

- `yes`: Customer subscribed
- `no`: Customer did not subscribe

The model can help the bank focus marketing efforts on customers who are more likely to subscribe.

## 1. Sample

The Bank Marketing dataset contained 11,162 records and 17 columns.

The data was divided using an 80/20 stratified split:

- Development sample: 8,929 records
- Holdout sample: 2,233 records

The development sample contained:

- `no`: 4,698 customers, or 52.62%
- `yes`: 4,231 customers, or 47.38%

The target classes were relatively balanced.

## 2. Explore

No missing values or duplicate records were found.

Categorical features included:

- `job`
- `marital`
- `education`
- `default`
- `housing`
- `loan`
- `contact`
- `month`
- `poutcome`

Numerical features included:

- `age`
- `balance`
- `day`
- `duration`
- `campaign`
- `pdays`
- `previous`

Subscription rates varied across job, education, marital status, housing, loan, contact method, and previous campaign outcome.

The numerical analysis showed that `balance` was right-skewed and contained outliers. Customers who subscribed generally had longer call durations. The `pdays` variable contained many `-1` values, indicating that customers had not previously been contacted.

## 3. Modify

The target variable was converted into binary values:

- `no` = `0`
- `yes` = `1`

The predictor variables were separated from the target.

The original data contained:

- 9 categorical features
- 7 numerical features
- 16 predictor columns

Categorical variables were transformed using one-hot encoding. Numerical variables were standardized using `StandardScaler`.

After preprocessing, the data contained 51 prepared features:

- Development data: 8,929 records and 51 features
- Holdout data: 2,233 records and 51 features

The preprocessing pipeline was fitted only on the development data and applied to the holdout data to prevent data leakage.

## 4. Model

The following classification models were trained:

- Logistic Regression
- Decision Tree
- Random Forest

## 5. Assess

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Random Forest | 0.858 | 0.825 | 0.888 | 0.855 | 0.920 |
| Logistic Regression | 0.826 | 0.828 | 0.800 | 0.813 | 0.907 |
| Decision Tree | 0.811 | 0.809 | 0.786 | 0.798 | 0.880 |

Random Forest was selected as the preferred model because it achieved the strongest overall performance.

### Random Forest Confusion Matrix

```text
[[976, 199],
 [119, 939]]```
```

## 6. Deployment

The saved Random Forest model and preprocessing pipeline are stored in:

- `SEMMA/models/semma_bank_random_forest.joblib`
- `SEMMA/models/semma_bank_preprocessor.joblib`
- `SEMMA/models/semma_deployment_config.joblib`

The deployment script is located at:

- `SEMMA/deployment/predict.py`

It can be executed with:

```bash
python3 SEMMA/deployment/predict.py```
