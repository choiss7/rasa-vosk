
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y ffmpeg build-essential libsndfile1
RUN pip install flask vosk
CMD ["python3", "app.py"]
