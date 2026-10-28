# SEMMA Bank Marketing Prediction

This project applies the SEMMA methodology to predict whether a bank customer will subscribe to a term deposit.

## Dataset

- Dataset: Bank Marketing Dataset
- Records: 11,162
- Features: 17
- Target: `deposit`

## SEMMA Phases

1. Sample
2. Explore
3. Modify
4. Model
5. Assess

## Best Model

Random Forest was selected as the best model.

- Accuracy: 0.858
- Precision: 0.825
- Recall: 0.888
- F1-score: 0.855
- ROC-AUC: 0.920

## Project Files

- Notebook: `notebooks/02_semma_bank_marketing.ipynb`
- Raw data: `data/raw/bank.csv`
- Final report: `reports/SEMMA_FINAL_REPORT.md`
- Data preparation: `reports/data-preparation.md`
- Models: `models/`
- Deployment script: `deployment/predict.py`


## Figures

The `figures/` directory contains the following analysis screenshots:

- `Categorical Feature Exploration by category.png`
- `Confusion matrix for all models.png`
- `customer subscription probability.png`
- `Model comparison.png`
- `Numerical features SEMMA.png`
- `SEMMA Modify phase.png`
- `Target Distribution.png`

## Deployment

Run from the repository root:

```bash
python3 SEMMA/deployment/predict.py
