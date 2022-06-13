import pyttsx3
import re
import speech_recognition as sr
from intentReader import intentReader
from pdfToAudio import transformPDFtoAudio
from telljoke import telljoke
from wrtieNote import note
from weather import weather
from listenAndSpeak import *

# check and write down note
def chekPraseForNote(text):
    speak("What you like me to write down ?")
    note_text = get_audio()
    note(note_text)
    speak("I've made a note of that.")


# check and read pdf book
def chekPraseForPDF(text):
    PDFREAD_STRS = ["pdf", "read", "reed"]
    for phrase in PDFREAD_STRS:
        if phrase in text:
            transformPDFtoAudio(speak)

def hello(text):
    return "hello someone"


#

# chekPraseForNote(text)
# chekPraseForPDF(text)
# chekPraseForJock(text)


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
