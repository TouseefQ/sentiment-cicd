from app import analyze_sentiment

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