import requests

# import asyncio

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "book")

if response:
    print(response.json())
else:
    print(f"Nothing retruned from: {BASE + 'book'}")
