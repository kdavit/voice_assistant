from listenAndSpeak import speak
from os import system


def openApplication(p):
    try:
        if ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p):
            system("chrome")
        elif ("IE" in p) or ("MSEDGE" in p) or ("EDGE" in p):
            system("msedge")
        elif ("NOTE" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p):
            system("Notepad")
        elif ("VLCPLAYER" in p) or ("PLAYER" in p) or ("VIDEO PLAYER" in p):
            system("VLC")
        elif ("ILLUSTRATOR" in p) or ("AI" in p):
            system("illustrator")
        elif ("PHOTOSHOP" in p) or ("PS" in p) or ("PHOTOSHOP CC" in p):
            system("photoshop")
        elif ("TELEGRAM" in p) or ("TG" in p):
            system("telegram")
        elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p) or ("WINEXCEL" in p):
            system("excel")
        elif ("SLIDE" in p) or ("MSPOWERPOINT" in p) or ("PPT" in p) or ("POWERPNT" in p):
            system("powerpnt")
        elif ("WORD" in p) or ("MSWORD" in p):
            system("winword")
        else:
            system("start {0}".format(p))
            return ""
    except:
        speak("Something went wrong.")
        return ""
