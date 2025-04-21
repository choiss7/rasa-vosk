import requests

# 테스트용 음성 파일 (16kHz, mono, wav)
AUDIO_FILE = "test_audio.wav"

url = "http://localhost:7000/asr"  # vosk_stt 서버의 엔드포인트

with open(AUDIO_FILE, "rb") as f:
    files = {"audio": f}
    response = requests.post(url, files=files)

print("STT 결과:", response.json()) 