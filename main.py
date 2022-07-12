import pyttsx3
import re
import speech_recognition as sr
from runassistent import runAssistent
from intentReader import intentReader
from pdfToAudio import transformPDFtoAudio
from hello import hello
from telljoke import telljoke
from wrtieNote import note
from weather import weather
from listenAndSpeak import *
from searchYoutube import searchYoutube
from worldNews import world_news
from open_application import openApplication
from WikiSearchThatSpeaks import wikiSearch



if __name__ == "__main__":
    while True:
        intent, text = runAssistent()
        if intent != 'No':
            speak(globals()[intent](text))
        print(intent, text)
