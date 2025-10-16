Sentiment Analyzer
A full-stack web application that analyzes the sentiment of text input using machine learning and natural language processing (NLP). Classify text as Positive, Negative, or Neutral with confidence scores in real-time.


🚀 Features
Real-time Sentiment Analysis: Instant classification of text as Positive, Negative, or Neutral

Confidence Scoring: Visual progress bars showing prediction confidence levels

Responsive Design: Works seamlessly on desktop and mobile devices

Input Validation: Ensures minimum 4-word requirement for accurate analysis

Beautiful UI: Modern gradient design with smooth animations

Error Handling: Comprehensive user feedback and error messages

🛠️ Tech Stack
Backend
Flask - Python web framework

Scikit-learn - Machine learning library

NLTK - Natural Language Toolkit for text processing

Naive Bayes - Multinomial NB classifier for sentiment classification

TF-IDF Vectorizer - Text feature extraction

Frontend
HTML5/CSS3 - Responsive web design with custom animations

Vanilla JavaScript - Client-side functionality and API calls

Modern CSS - CSS Grid, Flexbox, and gradient backgrounds

📁 Project Structure
text
sentiment-analyzer/
├── app.py                 # Flask application with ML model
├── package.json          # Node.js dependencies (if applicable)
├── static/
│   ├── style.css         # Responsive CSS styling
│   └── script.js         # Frontend JavaScript functionality
└── templates/
    └── index.html        # Main application interface
🎯 How It Works
Text Input: User enters text with at least 4 words

Preprocessing: Text is cleaned, lowercased, and punctuation removed

Feature Extraction: TF-IDF vectorization converts text to numerical features

Prediction: Trained Naive Bayes model classifies sentiment

Confidence Calculation: Model probabilities determine confidence scores

Result Display: Sentiment and confidence displayed with color-coded UI
