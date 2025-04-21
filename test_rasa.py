import requests

url = "http://localhost:5005/webhooks/rest/webhook"
data = {
    "sender": "test_user",
    "message": "안녕하세요"
}

response = requests.post(url, json=data)
print("Rasa 응답:", response.json()) 