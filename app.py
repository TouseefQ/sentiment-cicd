from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    """
    Core Logic: Returns 'Positive', 'Negative', or 'Neutral'
    """
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route('/')
def home():
    return "Sentiment Analysis API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text', '')
    sentiment = analyze_sentiment(text)
    return jsonify({'text': text, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)