from playsound import playsound
from gtts import gTTS
import sys

def main(filename):
    playsound(f"{filename}.mp3")


def make_soundfile(text):
    tts = gTTS(text=text, lang="en")
    tts.save(f"sound/{text}.mp3")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
    elif len(sys.argv) == 3:
        make_soundfile(sys.argv[1])



