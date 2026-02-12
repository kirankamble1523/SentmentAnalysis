🧠 Sentiment Analyzer (Flask + Machine Learning)

A simple and interactive Sentiment Analysis Web App built using Flask, Scikit-Learn, and NLP.
This application classifies text into Positive, Negative, or Neutral sentiments and provides a confidence score.

🚀 Live Demo (Optional)

Add your deployment link here if hosted (Render, Railway, Heroku, etc.)

📌 Features

🔍 Analyze text sentiment instantly

📊 Confidence score with animated progress bar

🎨 Modern and responsive UI

⚡ Real-time prediction using Fetch API

🤖 Machine Learning model (TF-IDF + Naive Bayes)

🛡 Input validation (minimum 2 words required)

🛠 Tech Stack
Backend

Python

Flask

Scikit-learn

NLTK

NumPy

Frontend

HTML5

CSS3 (Modern UI with animations)

JavaScript (Vanilla JS + Fetch API)

Deployment

Gunicorn (Production server)

📂 Project Structure
Sentiment-Analyzer/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md

⚙️ How It Works

User enters text in the textarea.

JavaScript sends a POST request to /predict.

Flask backend:

Preprocesses the text

Uses TF-IDF Vectorizer

Applies Multinomial Naive Bayes

Returns:

Sentiment (Positive/Negative/Neutral)

Confidence score

UI dynamically dis
