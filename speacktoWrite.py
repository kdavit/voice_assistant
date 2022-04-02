# Python program to translate
# speech to text and text to speech
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

activate =True
while (activate):
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            print("Silence please, calibratin bagrounde noise")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("calibrated, now speack ...")
            # listens for the user's input
            audio2 = r.listen(source2)
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            if MyText =="end writing":
                activate = False
            # write down in text file
            f = open("audioInTxt.txt", "a+")
            if MyText != "":
                 f.write(MyText+"\n")
            f.close()

            print("Did you say " + MyText)
            SpeakText(MyText)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
