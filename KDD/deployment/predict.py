from pathlib import Path

import joblib
import numpy as np
import pandas as pd


# Locate the KDD models folder
KDD_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = KDD_DIR / "models"

# Load the saved model and scaler
kmeans_model = joblib.load(
    MODEL_DIR / "kdd_kmeans_model.joblib"
)

scaler = joblib.load(
    MODEL_DIR / "kdd_scaler.joblib"
)

# Features used during clustering
clustering_features = [
    "Age",
    "Income",
    "Children_Total",
    "Recency",
    "Total_Spending",
    "Total_Purchases",
    "NumDealsPurchases",
    "NumWebVisitsMonth",
    "Total_Campaign_Accepted"
]

# Features that received log transformation during training
log_features = [
    "Income",
    "Total_Campaign_Accepted",
    "NumDealsPurchases"
]

# Example new customer
new_customer = pd.DataFrame({
    "Age": [45],
    "Income": [60000],
    "Children_Total": [1],
    "Recency": [30],
    "Total_Spending": [800],
    "Total_Purchases": [15],
    "NumDealsPurchases": [2],
    "NumWebVisitsMonth": [5],
    "Total_Campaign_Accepted": [1]
})

# Keep the exact training feature order
new_customer = new_customer[clustering_features]

# Apply the same log transformations used during training
new_customer_transformed = new_customer.copy()

for feature in log_features:
    new_customer_transformed[feature] = np.log1p(
        new_customer_transformed[feature]
    )

# Apply the saved scaler
new_customer_scaled = scaler.transform(
    new_customer_transformed
)

# Predict the customer cluster
predicted_cluster = int(
    kmeans_model.predict(new_customer_scaled)[0]
)

segment_names = {
    0: "Lower-spending customer segment",
    1: "Higher-value customer segment"
}

print("Predicted cluster:", predicted_cluster)
print("Customer segment:", segment_names[predicted_cluster])
