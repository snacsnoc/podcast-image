import requests
import json
import time

# Get lexica AI generated art by prompt
def image(prompt):
    results = requests.get("https://lexica.art/api/v1/search", params={"q": prompt})
    if results.status_code != 200:
        print("Requested URL: %s", results.url)
        print("Content: %s", results.content)
        results.raise_for_status()
    results = results.json()
    if results and results["images"]:
        response = {
            "src": results["images"][0]["src"],
            "alt": results["images"][0]["prompt"],
        }
        return response
    return {}


# Open output file for reading
with open("output-audio-file.txt", "r") as filehandle:
    output_audio_text = json.load(filehandle)

# Generate images per each value from our transcribed audio
images_list = []
for line in output_audio_text:
    a = image(line)
    images_list.append(a)
    time.sleep(1)
# Write image lists to file
if images_list != 0:
    with open("images-generated.json", "w") as f:
        json.dump(images_list, f, ensure_ascii=False)
