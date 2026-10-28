# Business Objective

The goal of this project is to predict whether a bank customer will subscribe to a term deposit after a marketing campaign.

The target variable is `deposit`:

- `yes`: Customer subscribed to a term deposit
- `no`: Customer did not subscribe to a term deposit

The target variable will be converted into binary values for modeling:

- `yes` = 1
- `no` = 0

## Business Value

The model can help the bank:

- Identify customers who are more likely to subscribe.
- Prioritize marketing outreach.
- Improve campaign efficiency.
- Reduce time and resources spent contacting unlikely subscribers.

## Success Criteria

Model performance will be evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrix

Because the `yes` class is slightly smaller than the `no` class, accuracy alone will not be sufficient. Recall and F1-score are especially important for measuring how effectively the model identifies potential subscribers.

## Project Scope

This project uses the Bank Marketing dataset and follows the SEMMA methodology:

1. Sample
2. Explore
3. Modify
4. Model
5. Assess

The final selected model will be saved and demonstrated through a deployment prediction script.
