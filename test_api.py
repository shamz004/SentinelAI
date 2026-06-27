import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "text": "CBI officer calling, your account is blocked, send OTP"
}

response = requests.post(url, json=data)
payload = response.json()

print("Status Code:", response.status_code)
print("Risk Level:", payload.get("risk_level"))
print("Category:", payload.get("category"))
print("Action:", payload.get("action"))
