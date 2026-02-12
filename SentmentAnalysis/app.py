from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import nltk
import os
import re

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


app = Flask(__name__)

# Training data
training_data = [
    ("This product is amazing and I love it", "Positive"),
    ("I am very happy with this purchase", "Positive"),
    ("Excellent service and great quality", "Positive"),
    ("This is the best experience ever", "Positive"),
    ("I absolutely adore this product", "Positive"),

    ("This product is terrible and awful", "Negative"),
    ("I hate this and it is useless", "Negative"),
    ("Very poor quality and bad service", "Negative"),
    ("This is the worst experience ever", "Negative"),
    ("I am very disappointed and upset", "Negative"),

    ("This product is okay and average", "Neutral"),
    ("It is what it is nothing special", "Neutral"),
    ("The product arrived on time today", "Neutral"),
    ("The price is reasonable and fair", "Neutral"),
    ("It works as described", "Neutral"),
]

texts = [t[0] for t in training_data]
labels = [t[1] for t in training_data]

model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", MultinomialNB())
])

model.fit(texts, labels)

def preprocess_text(text):
    text = text.lower()
    return re.sub(r"[^a-zA-Z\s]", "", text)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "").strip()

    if not text or len(text.split()) < 2:
        return jsonify({"error": "Please enter at least 2 words"}), 400

    cleaned = preprocess_text(text)
    prediction = model.predict([cleaned])[0]
    confidence = max(model.predict_proba([cleaned])[0]) * 100

    return jsonify({
        "sentiment": prediction,
        "confidence": round(confidence, 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
