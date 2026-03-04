import joblib

def predict(features):
    model = joblib.load("models/model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    scaled = scaler.transform([features])
    return int(model.predict(scaled)[0])
