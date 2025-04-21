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

## 참고
- 대용량 모델 파일은 깃허브에 포함되어 있지 않으니, 반드시 직접 다운로드 후 위 경로에 위치시켜야 합니다.
- 기타 문의: [Vosk 공식 문서](https://alphacephei.com/vosk/) 및 [Rasa 공식 문서](https://rasa.com/docs/) 