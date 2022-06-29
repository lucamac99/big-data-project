import requests
import json

url = 'http://localhost:8000/realestate'

f = open('scraped.json')
data = json.load(f)

for elem in data:
    requests.post(url, json=elem)