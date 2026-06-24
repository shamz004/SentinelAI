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

    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]

    result = "Positive 😊" if prediction == 1 else "Negative 😟"

    return jsonify({
        "input": text,
        "prediction": result
    })

if __name__ == "__main__":
    app.run(debug=True)