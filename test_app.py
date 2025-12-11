from app import analyze_sentiment, app
import pytest

def test_positive_sentiment():
    """Test if the model correctly identifies happy text"""
    text = "I love this product, it is amazing!"
    result = analyze_sentiment(text)
    assert result == "Positive"

def test_negative_sentiment():
    """Test if the model correctly identifies angry text"""
    text = "This is terrible and I hate it."
    result = analyze_sentiment(text)
    assert result == "Negative"

def test_neutral_sentiment():
    """Test if the model handles neutral text"""
    text = "The book is on the table."
    result = analyze_sentiment(text)
    assert result == "Neutral"

def test_empty_text():
    """Test if the model handles empty text"""
    text = ""
    result = analyze_sentiment(text)
    assert result is None

def test_text_too_long():
    """Test if the model rejects text that is too long"""
    text = "a" * 5001  # More than 5000 characters
    result = analyze_sentiment(text)
    assert result is None

def test_invalid_input_type():
    """Test if the model handles non-string input"""
    result = analyze_sentiment(None)
    assert result is None
    result = analyze_sentiment(123)
    assert result is None

def test_predict_endpoint_valid():
    """Test the /predict endpoint with valid input"""
    client = app.test_client()
    response = client.post('/predict', 
                          json={'text': 'This is great!'},
                          content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert 'sentiment' in data
    assert 'text' in data

def test_predict_endpoint_missing_text():
    """Test the /predict endpoint with missing text field"""
    client = app.test_client()
    response = client.post('/predict', 
                          json={},
                          content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_predict_endpoint_empty_text():
    """Test the /predict endpoint with empty text"""
    client = app.test_client()
    response = client.post('/predict', 
                          json={'text': ''},
                          content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_predict_endpoint_text_too_long():
    """Test the /predict endpoint with text that is too long"""
    client = app.test_client()
    text = "a" * 5001  # More than 5000 characters
    response = client.post('/predict', 
                          json={'text': text},
                          content_type='application/json')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data

def test_predict_endpoint_invalid_content_type():
    """Test the /predict endpoint with invalid content type"""
    client = app.test_client()
    response = client.post('/predict', 
                          data='text=hello',
                          content_type='application/x-www-form-urlencoded')
    assert response.status_code == 400

def test_security_headers():
    """Test that security headers are present"""
    client = app.test_client()
    response = client.get('/')
    assert 'X-Content-Type-Options' in response.headers
    assert response.headers['X-Content-Type-Options'] == 'nosniff'
    assert 'X-Frame-Options' in response.headers
    assert 'Content-Security-Policy' in response.headers