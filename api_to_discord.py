import requests

# API URL to fetch data from (using a public API for todos)
api_url = 'https://dummyjson.com/todos'

# Discord webhook URL
webhook_url = 'https://discord.com/api/webhooks/1351086319815888916/GkSxw4XAuJDCeshqZ95GBLYiwwgk7VCv3LFL7qDsPBIqXebwBshikJd8HcJm-9OT0H6B'

try:
    # Fetch data from the API
    response = requests.get(api_url)
    response.raise_for_status()  # Raise an error for bad status codes
    data = response.json()
    
    # Send the full JSON data as a string to Discord
    message = str(data)
    
    # Send the message to Discord webhook
    webhook_response = requests.post(webhook_url, json={'content': message})
    webhook_response.raise_for_status()
    
    print("Successfully sent data to Discord.")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
