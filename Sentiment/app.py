from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

app = Flask(__name__)

# Training data for sentiment analysis
training_data = [
    # Positive sentiments
    ("This product is amazing and I love it", "Positive"),
    ("I am very happy with this purchase", "Positive"),
    ("Excellent service and great quality", "Positive"),
    ("This is the best experience ever", "Positive"),
    ("I absolutely adore this product", "Positive"),
    ("Fantastic work and wonderful results", "Positive"),
    ("This made me so happy and satisfied", "Positive"),
    ("Outstanding quality and perfect service", "Positive"),
    ("I am delighted with this purchase", "Positive"),
    ("This is incredible and wonderful", "Positive"),
    
    # Negative sentiments
    ("This product is terrible and awful", "Negative"),
    ("I hate this and it is useless", "Negative"),
    ("Very poor quality and bad service", "Negative"),
    ("This is the worst experience ever", "Negative"),
    ("I am very disappointed and upset", "Negative"),
    ("Horrible product and waste of money", "Negative"),
    ("This is disgusting and unacceptable", "Negative"),
    ("Terrible customer service and rude staff", "Negative"),
    ("I regret buying this product", "Negative"),
    ("This is completely broken and useless", "Negative"),
    
    # Neutral sentiments
    ("This product is okay and average", "Neutral"),
    ("It is what it is nothing special", "Neutral"),
    ("The product arrived on time today", "Neutral"),
    ("This has some good and bad points", "Neutral"),
    ("The price is reasonable and fair", "Neutral"),
    ("It works as described in the listing", "Neutral"),
    ("The color is blue and the size is large", "Neutral"),
    ("This product has mixed reviews online", "Neutral"),
    ("The delivery took about five days", "Neutral"),
    ("It is similar to other products available", "Neutral"),
]

# Create and train the model
texts = [item[0] for item in training_data]
labels = [item[1] for item in training_data]

model = Pipeline([
    ('tfidf', TfidfVectorizer(lowercase=True, stop_words='english', max_features=100)),
    ('clf', MultinomialNB())
])

model.fit(texts, labels)

def preprocess_text(text):
    """Clean and preprocess text"""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

def predict_sentiment(text):
    """Predict sentiment of given text"""
    if len(text.split()) < 4:
        return {
            'sentiment': 'Invalid',
            'confidence': 0,
            'message': 'Please enter at least 4 words for analysis'
        }
    
    cleaned_text = preprocess_text(text)
    prediction = model.predict([cleaned_text])[0]
    probabilities = model.predict_proba([cleaned_text])[0]
    confidence = max(probabilities) * 100
    
    return {
        'sentiment': prediction,
        'confidence': round(confidence, 2),
        'message': f'Sentiment: {prediction} (Confidence: {round(confidence, 2)}%)'
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'error': 'Please enter some text'}), 400
    
    result = predict_sentiment(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
