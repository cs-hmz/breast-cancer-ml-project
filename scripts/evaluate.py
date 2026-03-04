import joblib
from sklearn.metrics import accuracy_score, classification_report
from preprocessing import preprocess_data
from sklearn.model_selection import train_test_split

X, y = preprocess_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = joblib.load("models/model.pkl")
y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(classification_report(y_test, y_pred))
