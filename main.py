import speech_recognition as sr
import pyttsx3
from telljock import *
from speacktoWrite import *

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
            # telljock(said)
            speakToText(said)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


text = get_audio()
# if "hello" in text:
# speak("hello someone")