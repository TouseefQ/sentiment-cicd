async function analyzeSentiment() {
    const text = document.getElementById('userInput').value;
    const resultDiv = document.getElementById('result');
    const sentimentLabel = document.getElementById('sentimentLabel');

    if (!text) {
        alert("Please enter some text first!");
        return;
    }

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
    const sentiment = data.sentiment;

    // 3. Update the UI
    sentimentLabel.innerText = `Sentiment: ${sentiment}`;
    
    // Reset classes
    resultDiv.className = '';
    resultDiv.classList.add(sentiment.toLowerCase()); // Adds 'positive', 'negative', or 'neutral' class
    
    // Show result
    resultDiv.style.display = 'block';
}