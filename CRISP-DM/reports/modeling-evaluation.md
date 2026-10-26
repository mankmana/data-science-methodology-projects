# CRISP-DM Phases 4 and 5: Modeling and Evaluation

## 1. Models Evaluated

Three classification models were trained:

- Logistic Regression
- Random Forest
- Gradient Boosting

All models used the same training and testing datasets and the same preprocessing pipeline.

## 2. Model Comparison

| Model | Accuracy | ROC-AUC | Churn Precision | Churn Recall | Churn F1-score |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.804 | 0.836 | 0.65 | 0.57 | 0.61 |
| Random Forest | 0.790 | 0.813 | 0.64 | 0.49 | 0.56 |
| Gradient Boosting | 0.796 | 0.839 | 0.64 | 0.53 | 0.58 |

## 3. Model Evaluation

Logistic Regression achieved the highest accuracy, churn recall, and churn F1-score.

Gradient Boosting achieved the highest ROC-AUC score, but its churn recall was lower than Logistic Regression.

Random Forest produced the lowest churn recall and missed the greatest number of actual churners.

## 4. Confusion Matrix Findings

Using the default threshold of 0.50:

- Logistic Regression correctly identified 214 churners and missed 160.
- Random Forest correctly identified 185 churners and missed 189.
- Gradient Boosting correctly identified 198 churners and missed 176.

Because missed churners represent missed retention opportunities, reducing false negatives is important.

## 5. Threshold Tuning

The following thresholds were tested:

| Threshold | Precision | Recall | F1-score |
|---:|---:|---:|---:|
| 0.30 | 0.511 | 0.759 | 0.611 |
| 0.40 | 0.579 | 0.684 | 0.627 |
| 0.50 | 0.648 | 0.572 | 0.608 |
| 0.60 | 0.679 | 0.385 | 0.491 |

A threshold of 0.40 was selected because it produced the highest F1-score while maintaining strong recall.

## 6. Final Model Selection

The final selected model is:

- Model: Logistic Regression
- Decision threshold: 0.40

This model was selected because it provides a practical balance between identifying potential churners and limiting unnecessary retention offers.

## 7. Limitations

- The dataset is historical and may not represent current customer behavior.
- The model does not prove that any feature causes churn.
- False positives may result in unnecessary retention costs.
- False negatives may result in missed retention opportunities.
- Model performance should be monitored after deployment.
