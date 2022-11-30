#!/usr/bin/python3
import os
import json
import sys
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)

if __name__ == "__main__":
    app.run(port=5000, debug=True)

basic_list = []
output_text = []
combined = []
# AI generated images
with open("images-generated.json", "r") as filehandle:
    basic_list = json.load(filehandle)

# Transcribed audio
with open("output-audio-file.txt", "r") as filehandle:
    output_text = json.load(filehandle)

combined = basic_list+output_text

@app.route("/", methods=["GET"])
def index():
    data = {"images": basic_list, "text": output_text,"combined":combined,}
    return render_template("index.html", data=data)

