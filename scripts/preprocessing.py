import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

def preprocess_data(path="data/data.csv"):
    data = pd.read_csv(path)
    data.drop(["Unnamed: 32", "id"], axis=1, inplace=True)
    data.diagnosis = [1 if value == 'M' else 0 for value in data.diagnosis]

    X = data.drop("diagnosis", axis=1)
    y = data["diagnosis"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    joblib.dump(scaler, "models/scaler.pkl")
    return X_scaled, y
