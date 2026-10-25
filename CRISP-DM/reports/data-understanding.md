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
