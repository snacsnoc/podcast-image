from vosk import Model, KaldiRecognizer
import wave
import json


wav_file = "test-split.wav"
model_path = "vosk-model-en-us-0.22"
model = Model(model_path)
wf = wave.open(wav_file, "rb")
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)


text_lst = []


while True:

    data = wf.readframes(4000)
    if len(data) == 0:
        break

    if rec.AcceptWaveform(data):
        word = json.loads(rec.Result())["text"]
        if len(word) > 0:
            text_lst.append(word)
            print("....new sentence...")

    else:
        print("....processing.......")


if text_lst != 0:
    with open("output-audio-file.txt", "w") as filehandle:
        json.dump(text_lst, filehandle)
