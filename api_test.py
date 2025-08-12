import requests

url = "http://localhost:8000/predict"
data = {"text": "Hello, AI"}

response = requests.post(url, json=data)
print(response.json())