from listenAndSpeak import speak
from os import system
def openApplication(applicationName):
    try:
        system("start {0}".format(applicationName))
        return ""
    except:
        speak("Could not find the application")
        return ""
