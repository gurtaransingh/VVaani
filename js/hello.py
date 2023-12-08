import requests

# The URL where your Flask app is listening
url = "http://4.240.66.128:8700/synthesize"

# The data you want to send (your text to synthesize)
data = {
    "text": "testing"
}

response = requests.post(url, json=data)

# Check the response
if response.status_code == 200:
    # If you expect the response to be an audio file:
    with open('3.wav', 'wb') as out_file:
        out_file.write(response.content)
    print("Audio saved to 3.wav")
else:
    print("Error:", response.status_code)
    print(response.text)