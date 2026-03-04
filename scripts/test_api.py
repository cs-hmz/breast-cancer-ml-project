import requests

url = "http://127.0.0.1:8000/predict"
sample_features = [14.2, 20.5, 92.1, 100.3, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,
                   0.7, 0.8, 0.9, 1.0, 2.1, 3.2, 4.3, 5.4, 6.5, 7.6,
                   8.7, 9.8, 10.9, 11.0, 12.1, 13.2, 14.3, 15.4, 16.5, 17.6]

response = requests.post(url, json={"features": sample_features})
print("Status:", response.status_code)
print("Response:", response.json())
