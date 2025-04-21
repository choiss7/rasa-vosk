import requests

# 1. 음성 파일을 Vosk STT에 전송
AUDIO_FILE = "test_audio.wav"
vosk_url = "http://localhost:7000/asr"

with open(AUDIO_FILE, "rb") as f:
    files = {"audio": f}
    stt_response = requests.post(vosk_url, files=files)

text = stt_response.json().get("text", "")
print("STT 결과:", text)

# 2. STT 결과를 Rasa 챗봇에 전송
rasa_url = "http://localhost:5005/webhooks/rest/webhook"
data = {
    "sender": "test_user",
    "message": text
}
rasa_response = requests.post(rasa_url, json=data)
print("Rasa 응답:", rasa_response.json()) 