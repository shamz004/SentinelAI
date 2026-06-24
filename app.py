import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    fraud_keywords = [
    "cbI officer", "digital arrest", "account blocked",
    "send otp", "verify bank", "urgent transfer"
]

if any(word.lower() in text.lower() for word in fraud_keywords):
    return jsonify({
        "input": text,
        "prediction": "FRAUD / SCAM 🚨 (Rule-based detection)"
    })

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

  if prediction == 1:
    result = "SAFE ✅"
elif prediction == 0:
    result = "SUSPICIOUS ⚠️"
else:
    result = "FRAUD / SCAM 🚨" 

    return jsonify({
        "input": text,
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)