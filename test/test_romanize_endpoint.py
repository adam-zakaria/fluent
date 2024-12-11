import requests
import os

# Summary: This code sends a POST request to the Romanize API and prints the response.
# Inputs: None
# Outputs: Prints the response from the API
#print({os.getenv("GOOGLE_CLOUD_ACCESS_TOKEN")})

response = requests.post(
    'http://localhost:3001/api/romanize',  # Ensure this matches your Flask app's URL
    json={'text': 'こんにちは', 'source_language': 'ja'}  # Replace with the text you want to romanize
)

print(response.json())  # Prints the JSON response from the API