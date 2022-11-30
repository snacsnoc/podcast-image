from pydub import AudioSegment


# input mp3 file
filename = "in.mp3"

# Output WAV file
dst = "out.wav"


# files
src = filename


# convert wav to mp3
print("Converting....\n")
sound = AudioSegment.from_mp3(src)
print("....Converting....\n")

# set to mono
sound = sound.set_channels(1)

sound.export(dst, format="wav")