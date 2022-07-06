import pyttsx3
import re
import speech_recognition as sr
from intentReader import intentReader
from pdfToAudio import transformPDFtoAudio
from telljoke import telljoke
from wrtieNote import note
from open_application import openApplication
from weather import weather
from worldNews import world_news
from listenAndSpeak import *

def hello(text):
    return "hello someone"

def runAssistent():
    text = get_audio()
    if "" in text:
        # text = text.replace("ben"," ").strip()
        text = text.strip()
        intentD = intentReader()
        for intent in intentD:
            for keyword in intentD[intent]:
                if keyword in text:
                    return intent, text.replace(keyword, "").strip()
    return "No", ""


if __name__ == "__main__":

    while True:
        intent, text = runAssistent()
        if intent != 'No':
            speak(globals()[intent](text))

        print(intent, text)
