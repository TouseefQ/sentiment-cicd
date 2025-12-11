// Security: Maximum text length constant (must match backend)
const MAX_TEXT_LENGTH = 5000;

async function analyzeSentiment() {
    const text = document.getElementById('userInput').value;
    const resultDiv = document.getElementById('result');
    const sentimentLabel = document.getElementById('sentimentLabel');

    if (!text) {
        alert("Please enter some text first!");
        return;
    }

    // Security: Validate text length on client side
    if (text.length > MAX_TEXT_LENGTH) {
        alert(`Text is too long. Maximum length is ${MAX_TEXT_LENGTH} characters.`);
        return;
    }

    try {
        // 1. Send the text to our Flask API
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });

        // 2. Get the answer
        const data = await response.json();
        
        // Security: Handle error responses from server
        if (!response.ok || data.error) {
            alert(data.error || 'An error occurred while analyzing the text.');
            return;
        }
        
        const sentiment = data.sentiment;

        // 3. Update the UI (using textContent for security)
        sentimentLabel.textContent = `Sentiment: ${sentiment}`;
        
        // Reset classes
        resultDiv.className = '';
        resultDiv.classList.add(sentiment.toLowerCase()); // Adds 'positive', 'negative', or 'neutral' class
        
        // Show result
        resultDiv.style.display = 'block';
    } catch (error) {
        // Security: Handle network errors gracefully
        alert('Failed to analyze sentiment. Please try again.');
        console.error('Error:', error);
    }
}