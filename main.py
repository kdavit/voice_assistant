import speech_recognition as sr
import pyttsx3
from telljock import *
from pdfToAudio import transformPDFtoAudio

from wrtieNote import note

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()

text = get_audio()


if "hello" in text:
    speak("hello someone")
# write down note
NOTE_STRS = ["make a note","make a note","write this down","remeber this","write note","write a note"]
for phrase in NOTE_STRS:
    if phrase in text:
        speak("What you like me to write down ?")
        note_text = get_audio()
        note(note_text)
        speak("I've made a note of that.")

# read pdf book
PDFREAD_STRS = ["read a pdf","read a book","read","pdf read","read pdf book"]
for phrase in PDFREAD_STRS:
    if phrase in text:
        transformPDFtoAudio(speak,get_audio)
