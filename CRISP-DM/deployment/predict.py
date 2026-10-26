from pathlib import Path
import joblib
import pandas as pd

project_dir = Path(__file__).resolve().parents[1]
models_dir = project_dir / "models"

preprocessor = joblib.load(models_dir / "telco_preprocessor.joblib")
model = joblib.load(models_dir / "telco_churn_logistic_model.joblib")
config = joblib.load(models_dir / "deployment_config.joblib")

customer = pd.DataFrame([{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 12,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "Yes",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 70.35,
    "TotalCharges": 845.50
}])

prepared_customer = preprocessor.transform(customer)
churn_probability = model.predict_proba(prepared_customer)[0, 1]
threshold = config["threshold"]

prediction = (
    "Likely to churn"
    if churn_probability >= threshold
    else "Likely to stay"
)

print(f"Churn probability: {churn_probability:.2%}")
print(f"Prediction: {prediction}")
print(f"Decision threshold: {threshold}")
