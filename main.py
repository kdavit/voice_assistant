import pyttsx3
import re
import speech_recognition as sr
from intentReader import intentReader
from pdfToAudio import transformPDFtoAudio
from telljoke import telljoke
from wrtieNote import note
from weather import weather
from listenAndSpeak import *
from searchYoutube import searchYoutube
from worldNews import world_news
from open_application import openApplication
from WikiSearchThatSpeaks import wikiSearch

def hello(text):
    return "hello someone"


def runAssistent():
    text = get_audio()
    if "anna" in text:
        text = text.replace("anna", "").strip()
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
