import pyttsx3
import re
import speech_recognition as sr
from intentReader import intentReader
from pdfToAudio import transformPDFtoAudio
from telljoke import telljoke
from wrtieNote import note


# speak the text
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


# listen to command
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


# check and tell jock
def chekPraseForJock(text):
    comand = re.search("(joke|funny|humorous)", text)
    if comand:
        telljock(text, speak)

def hello(text) :
    return "hello someone"
#

# chekPraseForNote(text)
# chekPraseForPDF(text)
# chekPraseForJock(text)


def runAssistent():
    text = get_audio()
    if "ben" in text:
        text = text.replace("ben", "").strip()
        intentD = intentReader()
        for intent in intentD:
            for keyword in intentD[intent]:
                if keyword in text:
                    return intent, text.replace(keyword, "").strip()
    return "No", ""


while True:
    intent, text = runAssistent()
    if intent != 'No':
        speak(globals()[intent](text))

    print (intent, text)
