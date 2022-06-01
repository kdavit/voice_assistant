# Python program to translate
# speech to text and text to speech
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
def speakToText(said):
    def SpeakText(command):
        # Initialize the engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    try:
        if said =="end writing":
            activate = False
        # write down in text file
        f = open("audioInTxt.txt", "a+")
        if said != "":
             f.write(said+"\n")
        f.close()

        print("Did you say " + said)
        SpeakText(said)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
