import subprocess

print("1. Vosk STT 테스트")
subprocess.run(["python", "test_vosk_stt.py"])

print("\n2. Rasa 챗봇 테스트")
subprocess.run(["python", "test_rasa.py"])

print("\n3. 전체 파이프라인 테스트")
subprocess.run(["python", "test_full_pipeline.py"]) 