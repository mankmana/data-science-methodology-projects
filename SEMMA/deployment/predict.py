from pathlib import Path

import joblib
import pandas as pd


# Locate the SEMMA project directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]
MODEL_DIR = PROJECT_ROOT / "models"

# Load the saved model artifacts
model = joblib.load(
    MODEL_DIR / "semma_bank_random_forest.joblib"
)

preprocessor = joblib.load(
    MODEL_DIR / "semma_bank_preprocessor.joblib"
)

config = joblib.load(
    MODEL_DIR / "semma_deployment_config.joblib"
)

# Create an example customer record
customer = pd.DataFrame([{
    "age": 40,
    "job": "management",
    "marital": "married",
    "education": "tertiary",
    "default": "no",
    "balance": 1500,
    "housing": "yes",
    "loan": "no",
    "contact": "cellular",
    "day": 15,
    "month": "may",
    "duration": 300,
    "campaign": 1,
    "pdays": -1,
    "previous": 0,
    "poutcome": "unknown"
}])

# Apply the same preprocessing used during model training
customer_prepared = preprocessor.transform(customer)

# Calculate subscription probability
subscription_probability = model.predict_proba(
    customer_prepared
)[0, 1]

# Use the configured threshold, or 0.50 by default
decision_threshold = config.get(
    "decision_threshold",
    0.50
)

prediction = int(
    subscription_probability >= decision_threshold
)

# Display the result
print(
    f"Deposit subscription probability: "
    f"{subscription_probability:.2%}"
)

if prediction == 1:
    print("Prediction: Likely to subscribe")
else:
    print("Prediction: Likely not to subscribe")

print(
    f"Decision threshold: {decision_threshold}"
)
