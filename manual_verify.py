import requests

url = "https://sentiment-cicd-touseefq.onrender.com/predict"

print(f"Testing URL: {url}")

payload = {"text": "I absolutely love this amazing service!"}

try:
    response = requests.post(url, json=payload)
    
    print(f"\nStatus Code: {response.status_code}")
    print(f"Raw Output: {response.text[:200]}") # Print first 200 chars to see if it's HTML
    
    # Try to parse JSON only if the status is 200 (OK)
    if response.status_code == 200:
        print(f"JSON Response: {response.json()}")
    else:
        print("❌ Error: The server returned a failure code.")

except Exception as e:
    print(f"Connection failed: {e}")