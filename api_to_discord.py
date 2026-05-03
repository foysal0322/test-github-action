import requests

# API URL to fetch data from (using a public API for random quotes)
api_url = 'https://api.quotable.io/random'

# Discord webhook URL
webhook_url = 'https://discord.com/api/webhooks/1351086319815888916/GkSxw4XAuJDCeshqZ95GBLYiwwgk7VCv3LFL7qDsPBIqXebwBshikJd8HcJm-9OT0H6B'

try:
    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()
    
    # Extract the quote content (assuming the API returns a JSON with 'content' key)
    message = data.get('content', 'No content available')
    
    # Send the message to Discord webhook
    webhook_response = requests.post(webhook_url, json={'content': message})
    webhook_response.raise_for_status()
    
    print("Successfully sent data to Discord.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
