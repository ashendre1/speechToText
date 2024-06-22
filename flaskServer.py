import speech_recognition as sr
from flask import Flask, request
import io, base64

def speechToTextFunction(path):
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        r.adjust_for_ambient_noise(source)
        audio_listened = r.listen(source)

    try:
        rec = r.recognize_google(audio_listened)
        return rec

    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Could not request results. check your internet connection")


app = Flask(__name__)

@app.route('/convert', methods = ["POST"])
def convert():
    print('inside convert')
    audio_base64 = request.json['audio']
    audio_data = base64.b64decode(audio_base64)
    audio_file = io.BytesIO(audio_data)
    audio_recognized = speechToTextFunction(audio_file)
    return audio_recognized



if __name__ == '__main__':
    app.run()

