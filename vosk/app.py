
from flask import Flask, request, jsonify
from vosk import Model, KaldiRecognizer
import wave

app = Flask(__name__)
model = Model("vosk-model-small-ko-0.22")

@app.route('/stt', methods=['POST'])
def stt():
    file = request.files['audio']
    wf = wave.open(file, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    results = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(rec.Result())

    final = rec.FinalResult()
    return jsonify({"text": eval(final).get("text", "")})
