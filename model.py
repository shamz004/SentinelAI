from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# sample training data (simple AI dataset)
texts = [
    "I am happy",
    "I feel good",
    "I am sad",
    "I am stressed",
    "I am angry",
    "I feel great"
]

labels = [
    1,  # positive
    1,
    0,  # negative
    0,
    0,
    1
]

# convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# train model
model = LogisticRegression()
model.fit(X, labels)

# save model
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model created successfully!")