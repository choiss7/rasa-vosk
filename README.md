# rasa-vosk

Rasa + Vosk 연동 프로젝트

## 프로젝트 개요
- Rasa(챗봇)와 Vosk(음성 인식)를 연동하여 한국어 음성 챗봇을 구현하는 예제입니다.

## 구성 요소
- Rasa: 대화 관리 및 자연어 처리
- Vosk: 오픈소스 음성 인식 엔진
- Docker Compose: 서비스 오케스트레이션

## 사용 방법

### 1. Vosk 한국어 모델 다운로드

1. [Vosk 공식 모델 다운로드 페이지](https://alphacephei.com/vosk/models)에서 `vosk-model-small-ko-0.22`를 다운로드합니다.
2. 압축을 해제하여 `vosk/vosk-model-small-ko-0.22` 폴더에 위치시킵니다.
   - 최종 폴더 구조 예시:
     ```
     vosk/
       ├── Dockerfile
       ├── app.py
       └── vosk-model-small-ko-0.22/
            ├── am/
            ├── conf/
            ├── graph/
            └── ...
     ```

### 2. 도커 컴포즈로 실행

```bash
docker-compose up --build
```

- Rasa: http://localhost:5005
- Action Server: http://localhost:5055
- Vosk STT: http://localhost:7000

---

## 테스트 실행 방법

1. **테스트용 음성 파일 준비**
   - `test_audio.wav` (16kHz, mono, 짧은 한국어 음성)
   - 예: 네이버 클로바더빙 등에서 "안녕하세요" TTS로 생성 후 wav로 변환
   - 프로젝트 루트에 위치

2. **테스트 자동화 스크립트 실행**
   ```bash
   python run_all_tests.py
   ```
   - Vosk STT, Rasa 챗봇, 전체 파이프라인 테스트가 순차적으로 실행됩니다.

3. **개별 테스트 실행도 가능**
   ```bash
   python test_vosk_stt.py
   python test_rasa.py
   python test_full_pipeline.py
   ```

---

## 참고
- 대용량 모델 파일은 깃허브에 포함되어 있지 않으니, 반드시 직접 다운로드 후 위 경로에 위치시켜야 합니다.
- 기타 문의: [Vosk 공식 문서](https://alphacephei.com/vosk/) 및 [Rasa 공식 문서](https://rasa.com/docs/) 