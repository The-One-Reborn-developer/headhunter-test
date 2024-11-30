import wave
import json
import os

from flask import Flask, request, jsonify

from vosk import Model, KaldiRecognizer

from pydub import AudioSegment


app = Flask(__name__)


VOSK_MODEL_PATH = "vosk-model-small-ru-0.22"


model = Model(VOSK_MODEL_PATH)


def transcribe_audio(file_path):
    audio = AudioSegment.from_file(file_path, format="mp3")
    wav_path = file_path.replace(".mp3", ".wav")
    audio.export(wav_path, format="wav")

    wf = wave.open(wav_path, "rb")
    
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    results.append(json.loads(rec.FinalResult()))
    wf.close()
    return results


def analyze_results(results):
    dialog = []
    total_duration = {"receiver": 0, "transmitter": 0}

    roles = ["receiver", "transmitter"]
    sex = ["male", "female"]
    role_index = 0

    for result in results:
        if "text" in result and result["text"]:
            text = result["text"]
            duration = len(text.split())
            raised_voice = "!" in text
            gender = sex[role_index % 2]
            source = roles[role_index % 2]

            dialog.append({
                "source": source,
                "text": text,
                "duration": duration,
                "raised_voice": raised_voice,
                "gender": gender
            })

            total_duration[source] += duration
            role_index += 1

    return dialog, total_duration


@app.route('/', methods=['POST'])
def handle_audio_recognition():
    data = request.get_json()
    file_path = data.get("file_path")

    if not file_path or not os.path.exists(file_path):
        return jsonify({"error": "Файл не найден"}), 400

    try:
        results = transcribe_audio(file_path)
        dialog, result_duration = analyze_results(results)
        response = {
            "dialog": dialog,
            "result_duration": result_duration
        }
        return app.response_class(
            json.dumps(response, ensure_ascii=False, indent=4),
            status=200,
            mimetype='application/json',
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
