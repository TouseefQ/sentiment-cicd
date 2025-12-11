from flask import Flask, request, jsonify, render_template
from textblob import TextBlob
import html

app = Flask(__name__)

# Security: Disable debug mode explicitly
app.config['DEBUG'] = False

# Security: Set maximum content length to prevent DoS (1MB limit)
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

# Security: Maximum text length for sentiment analysis
MAX_TEXT_LENGTH = 5000

# Security: Add security headers to all responses
@app.after_request
def add_security_headers(response):
    # Prevent XSS attacks
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    # Content Security Policy (Note: 'unsafe-inline' for styles is a trade-off for simplicity)
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'"
    # HSTS: Only meaningful over HTTPS, but set for production readiness
    if request.is_secure:
        response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    return response

def analyze_sentiment(text):
    # Security: Validate input is not empty
    if not text or not isinstance(text, str):
        return None
    
    # Security: Limit text length to prevent resource exhaustion
    if len(text) > MAX_TEXT_LENGTH:
        return None
    
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
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Security: Validate request has JSON content type
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.get_json()
    
    # Security: Validate input data
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing required field: text'}), 400
    
    text = data.get('text', '')
    
    # Security: Validate text is string type
    if not isinstance(text, str):
        return jsonify({'error': 'Text must be a string'}), 400
    
    # Security: Validate text length
    if len(text) == 0:
        return jsonify({'error': 'Text cannot be empty'}), 400
    
    if len(text) > MAX_TEXT_LENGTH:
        return jsonify({'error': f'Text is too long. Maximum length is {MAX_TEXT_LENGTH} characters'}), 400
    
    sentiment = analyze_sentiment(text)
    
    if sentiment is None:
        return jsonify({'error': 'Failed to analyze sentiment'}), 500
    
    # Security: Sanitize output to prevent XSS (escape HTML entities)
    safe_text = html.escape(text)
    
    return jsonify({'text': safe_text, 'sentiment': sentiment})

if __name__ == '__main__':
    # Security: Explicitly set debug to False for production
    app.run(host='0.0.0.0', port=5000, debug=False)