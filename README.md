# podcast-image
![screenshot](https://geekness.eu/sites/default/files/screenshot-podcast-image.jpg)
Use AI generated images created from prompts transcribed from audio, in this case podcasts. This project is very unfinished, but it works.

`convert.py` convert MP3 to mono WAV

`transcribe.py` uses [Vosk](https://alphacephei.com/vosk/) for speach recognition. We feed it an input wav file and get a `output-audio-file.txt`

`generate-art-from-list.py` use [Lexica.art](https://lexica.art) to get images from our input text file and output to `images-generated.json`

# Flask app

Included is a very simple Flask app, see `app.py`. 