from flask import Flask, request, jsonify, render_template
import os
import uuid

from modules.currency_detection import detect_currency
from modules.geo_dashboard import get_geo_data
from modules.network_analysis import get_fraud_network
from modules.voice_detector import VoiceDetector
from modules.risk_engine import analyze_risk

app = Flask(__name__)

# ---------------- INITIALIZE MODELS ----------------
detector = VoiceDetector()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- MAIN PAGE ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- DASHBOARD PAGE ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- TEXT RISK PREDICTION ---------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True) or {}
    text = data.get("text", "")

    result = analyze_risk(text)

    return jsonify({
        "input": text,
        "risk_level": result["risk"],
        "category": result["category"],
        "action": result["action"],
        "confidence": result.get("confidence", 0.91 if result["risk"] == "HIGH" else 0.74)
    })


# ---------------- GEO DATA API ----------------
@app.route("/geo-data")
def geo_data():
    return jsonify(get_geo_data())


# ---------------- NETWORK DATA API ----------------
@app.route("/network-data")
def network_data():
    return jsonify({"edges": get_fraud_network()})


# ---------------- VOICE CHECK API ----------------
@app.route("/voice-check", methods=["POST"])
def voice_check():

    if "file" not in request.files:
        return jsonify({
            "error": "No file received",
            "received_keys": list(request.files.keys())
        }), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename received"}), 400

    # Use a generated filename so uploaded audio cannot overwrite local files.
    filename = str(uuid.uuid4()) + ".wav"
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    try:
        result = detector.analyze(filepath)
        return jsonify(result)

    except Exception as e:
        return jsonify({
            "error": "Voice analysis failed",
            "details": str(e)
        }), 500


# ---------------- CURRENCY CHECK API ----------------
@app.route("/currency-check", methods=["POST"])
def currency_check():

    if "currency_image" not in request.files:
        return jsonify({"error": "No image received"}), 400

    file = request.files["currency_image"]

    if file.filename == "":
        return jsonify({"error": "Empty filename received"}), 400

    filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    file.save(filepath)

    result = detect_currency(filepath)

    return jsonify({
        "result": result
    })


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
