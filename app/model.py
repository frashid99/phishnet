import joblib

model = joblib.load('models/phishing_model.pkl')

def predict_email(text: str) -> str:
    proba = model.predict_proba([text])[0]
    label = "Phishing" if proba[1] >= 0.5 else "Legitimate"
    confidence = round(max(proba) * 100, 2)
    return label, confidence
