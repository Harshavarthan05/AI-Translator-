from gtts import gTTS
from playsound import playsound
import os

def speech_text(txt, lang):
    try:
        speech = gTTS(text = txt, lang = lang, slow = False)

        speech.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")

    except Exception as e:
        print("Speech Error: ",e)