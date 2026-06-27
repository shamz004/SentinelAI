import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from modules.data_preprocess import load_dataset

MODEL_PATH = "modules/fraud_model.pkl"


class FraudModel:

    def train(self):
        df = load_dataset()

        X = df["text"]
        y = df["label"]

        vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
        X_vec = vectorizer.fit_transform(X)

        model = LogisticRegression(max_iter=1000)
        model.fit(X_vec, y)

        joblib.dump((vectorizer, model), MODEL_PATH)

        print("Model trained successfully!")

    def predict(self, text):

        vectorizer, model = joblib.load(MODEL_PATH)

        X_vec = vectorizer.transform([text])
        pred = model.predict(X_vec)[0]

        proba = model.predict_proba(X_vec).max()

        return {
            "prediction": "FRAUD" if pred == 1 else "SAFE",
            "confidence": round(float(proba), 3)
        }