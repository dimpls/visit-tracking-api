import requests

url = 'http://127.0.0.1:8000/api/visits/create/1/'
data = {
    'latitude': 123.456,
    'longitude': 789.012
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
